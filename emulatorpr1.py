#!/usr/bin/env python3
import os
import sys
import csv
import base64
import argparse
import tkinter as tk
from tkinter import scrolledtext


class VFSNode:
    __slots__ = ("name", "is_dir", "size", "content", "children")

    def __init__(self, name, is_dir=False, size=0, content=b""):
        self.name = name
        self.is_dir = is_dir
        self.size = size
        self.content = content
        self.children = {}


class VFS:
    EXPECTED_HEADER = ["type", "name", "parent", "size", "content"]

    def __init__(self):
        self.root = VFSNode("/", is_dir=True)

    def load_csv(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"file not found: {path}")
        if not os.path.isfile(path):
            raise ValueError(f"not a file: {path}")

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
            except StopIteration:
                raise ValueError("empty CSV file")
            header_norm = [h.strip().lower() for h in header]
            if header_norm != self.EXPECTED_HEADER:
                raise ValueError(
                    f"invalid header {header}, expected {self.EXPECTED_HEADER}"
                )
            rows = [r for r in reader if r and any(c.strip() for c in r)]

        rows.sort(key=lambda r: r[2].count("/"))

        for idx, row in enumerate(rows, start=2):
            if len(row) < 5:
                raise ValueError(f"row {idx}: not enough columns: {row}")
            typ, name, parent, size, content = (c.strip() for c in row[:5])
            typ = typ.lower()
            if typ not in ("dir", "file"):
                raise ValueError(f"row {idx}: unknown type '{typ}'")
            is_dir = (typ == "dir")
            try:
                sz = int(size) if size else 0
            except ValueError:
                raise ValueError(f"row {idx}: bad size '{size}'")
            data = b""
            if not is_dir and content:
                try:
                    data = base64.b64decode(content, validate=True)
                except Exception as e:
                    raise ValueError(f"row {idx}: bad base64 ({e})")
            self._add_node(parent, name, is_dir, sz, data)

    def _add_node(self, parent_path, name, is_dir, size, content):
        parent = self._resolve(parent_path)
        if parent is None:
            raise ValueError(f"parent path '{parent_path}' not found")
        if not parent.is_dir:
            raise ValueError(f"parent '{parent_path}' is not a directory")
        if name in parent.children:
            raise ValueError(f"duplicate name '{name}' in '{parent_path}'")
        parent.children[name] = VFSNode(name, is_dir, size, content)

    def _resolve(self, path):
        stack = []
        for p in path.split("/"):
            if not p or p == ".":
                continue
            if p == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(p)
        node = self.root
        for p in stack:
            if not node.is_dir or p not in node.children:
                return None
            node = node.children[p]
        return node

    def list_dir(self, path):
        node = self._resolve(path)
        if node is None:
            return None, f"ls: cannot access '{path}': No such file or directory"
        if not node.is_dir:
            return [(node.name, False, node.size)], None
        items = [(n, c.is_dir, c.size) for n, c in sorted(node.children.items())]
        return items, None


class Emulator:
    def __init__(self, root, vfs_path=None, script_path=None):
        self.root = root
        self.vfs = VFS()
        self.cwd = "/"
        self.vfs_path = vfs_path
        self.script_path = script_path
        self.vfs_loaded = False
        self.pending_error = None

        if vfs_path:
            try:
                self.vfs.load_csv(vfs_path)
                self.vfs_loaded = True
            except Exception as e:
                self.pending_error = f"VFS load error: {e}"

        self._build_ui()
        if self.pending_error:
            self.write(self.pending_error)

    def _build_ui(self):
        self.root.title("VFS")
        self.root.geometry("900x520")

        self.output = scrolledtext.ScrolledText(
            self.root, height=25, width=110, state="disabled",
            bg="black", fg="#d0ffd0", insertbackground="white",
            font=("Courier New", 10),
        )
        self.output.pack(fill="both", expand=True)

        frame = tk.Frame(self.root)
        frame.pack(fill="x")
        self.prompt_label = tk.Label(frame, text=self.prompt(),
                                     font=("Courier New", 10))
        self.prompt_label.pack(side="left")
        self.entry = tk.Entry(frame, font=("Courier New", 10))
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", self.on_enter)
        self.entry.focus_set()

    def prompt(self):
        return f"user@vfs:{self.cwd}$ "

    def write(self, text):
        self.output.configure(state="normal")
        self.output.insert("end", str(text) + "\n")
        self.output.see("end")
        self.output.configure(state="disabled")

    def on_enter(self, _event):
        line = self.entry.get()
        self.entry.delete(0, "end")
        self.process_line(line, echo=True)

    def process_line(self, line, echo=False):
        if echo:
            self.write(self.prompt() + line)
        line = line.strip()
        if not line:
            return True
        parts = line.split()
        cmd, args = parts[0], parts[1:]
        try:
            return self.run_command(cmd, args)
        except Exception as e:
            self.write(f"internal error: {e}")
            return True

    def run_command(self, cmd, args):
        if cmd == "exit":
            self.root.quit()
            self.root.destroy()
            return False
        handlers = {
            "ls":        self.cmd_ls,
            "cd":        self.cmd_cd,
            "cat":       self.cmd_cat,
            "pwd":       self.cmd_pwd,
            "conf-dump": self.cmd_conf_dump,
            "help":      self.cmd_help,
        }
        handler = handlers.get(cmd)
        if handler is None:
            self.write(f"{cmd}: command not found")
            return True
        handler(args)
        return True

    def cmd_ls(self, args):
        path = args[0] if args else self.cwd
        items, err = self.vfs.list_dir(self.resolve_path(path))
        if err:
            self.write(err)
            return
        for name, is_dir, size in items:
            self.write(f"{name}{'/' if is_dir else ''}")

    def cmd_cd(self, args):
        target = args[0] if args else "/"
        new_path = self.resolve_path(target)
        node = self.vfs._resolve(new_path)
        if node is None:
            self.write(f"cd: {target}: No such file or directory")
        elif not node.is_dir:
            self.write(f"cd: {target}: Not a directory")
        else:
            self.cwd = new_path
            self.prompt_label.config(text=self.prompt())

    def cmd_cat(self, args):
        if not args:
            self.write("cat: missing operand")
            return
        target = args[0]
        node = self.vfs._resolve(self.resolve_path(target))
        if node is None:
            self.write(f"cat: {target}: No such file or directory")
        elif node.is_dir:
            self.write(f"cat: {target}: Is a directory")
        else:
            try:
                self.write(node.content.decode("utf-8"))
            except UnicodeDecodeError:
                self.write(f"cat: {target}: binary content ({len(node.content)} bytes)")

    def cmd_pwd(self, args):
        self.write(self.cwd)

    def cmd_conf_dump(self, args):
        self.write(f"vfs.path    = {self.vfs_path or '(none)'}")
        self.write(f"script.path = {self.script_path or '(none)'}")
        self.write(f"vfs.loaded  = {self.vfs_loaded}")
        self.write(f"cwd         = {self.cwd}")

    def cmd_help(self, args):
        self.write("commands: ls, cd, cat, pwd, conf-dump, help, exit")

    def resolve_path(self, path):
        if path.startswith("/"):
            base = path
        else:
            base = self.cwd.rstrip("/") + "/" + path
        stack = []
        for p in base.split("/"):
            if not p or p == ".":
                continue
            if p == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(p)
        return "/" + "/".join(stack)

    def run_script(self, path):
        if not os.path.exists(path):
            self.write(f"script: file not found: {path}")
            return
        self.write(f"# executing script: {path}")
        with open(path, encoding="utf-8") as f:
            for raw in f:
                line = raw.rstrip("\n")
                if not line.strip() or line.strip().startswith("#"):
                    continue
                self.process_line(line, echo=True)


def parse_args():
    p = argparse.ArgumentParser(description="VFS shell emulator (GUI)")
    p.add_argument("--vfs-path", default=None, help="path to VFS CSV file")
    p.add_argument("--script",   default=None, help="path to startup script")
    return p.parse_args()


def main():
    args = parse_args()

    print("=== emulator configuration ===")
    print(f"vfs.path    = {args.vfs_path}")
    print(f"script.path = {args.script}")
    print("==============================")

    root = tk.Tk()
    emu = Emulator(root, vfs_path=args.vfs_path, script_path=args.script)

    if args.script:
        root.after(150, lambda: emu.run_script(args.script))

    root.mainloop()


if __name__ == "__main__":
    main()
