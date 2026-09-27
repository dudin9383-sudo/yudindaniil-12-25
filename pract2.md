# Практическое занятие №2. Менеджеры пакетов
Юдин Д.А.

Разобраться, что представляет собой менеджер пакетов, как устроен пакет, как читать версии стандарта semver. Привести примеры программ, в которых имеется встроенный пакетный менеджер.

## Задача 1
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?

Команда
```
wget https://files.pythonhosted.org/packages/source/m/matplotlib/matplotlib-3.11.2.tar.gz
pip install ./matplotlib-3.11.2.tar.gz
pip show matplotlib
```
Вывод
```
Name: matplotlib
Version: 3.11.2
Summary: Python plotting package
Home-page:
Author: John D. Hunter, Michael Droettboom
Author-email: Unknown <matplotlib-users@python.org>
License: License agreement for matplotlib versions 1.3.0 and later
 =========================================================

 1. This LICENSE AGREEMENT is between the Matplotlib Development Team
 ("MDT"), and the Individual or Organization ("Licensee") accessing and
 otherwise using matplotlib software in source or binary form and its
 associated documentation.

 2. Subject to the terms and conditions of this License Agreement, MDT
 hereby grants Licensee a nonexclusive, royalty-free, world-wide license
 to reproduce, analyze, test, perform and/or display publicly, prepare
 derivative works, distribute, and otherwise use matplotlib
 alone or in any derivative version, provided, however, that MDT's
 License Agreement and MDT's notice of copyright, i.e., "Copyright (c)
 2012- Matplotlib Development Team; All Rights Reserved" are retained in
 matplotlib  alone or in any derivative version prepared by
 Licensee.

 3. In the event Licensee prepares a derivative work that is based on or
 incorporates matplotlib or any part thereof, and wants to
 make the derivative work available to others as provided herein, then
 Licensee hereby agrees to include in any such work a brief summary of
 the changes made to matplotlib .

 4. MDT is making matplotlib available to Licensee on an "AS
 IS" basis.  MDT MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
 IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, MDT MAKES NO AND
 DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
 FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF MATPLOTLIB
 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

 5. MDT SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF MATPLOTLIB
  FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR
 LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING
 MATPLOTLIB , OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF
 THE POSSIBILITY THEREOF.

 6. This License Agreement will automatically terminate upon a material
 breach of its terms and conditions.

 7. Nothing in this License Agreement shall be deemed to create any
 relationship of agency, partnership, or joint venture between MDT and
 Licensee.  This License Agreement does not grant permission to use MDT
 trademarks or trade name in a trademark sense to endorse or promote
 products or services of Licensee, or any third party.

 8. By copying, installing or otherwise using matplotlib ,
 Licensee agrees to be bound by the terms and conditions of this License
 Agreement.

 License agreement for matplotlib versions prior to 1.3.0
 ========================================================

 1. This LICENSE AGREEMENT is between John D. Hunter ("JDH"), and the
 Individual or Organization ("Licensee") accessing and otherwise using
 matplotlib software in source or binary form and its associated
 documentation.

 2. Subject to the terms and conditions of this License Agreement, JDH
 hereby grants Licensee a nonexclusive, royalty-free, world-wide license
 to reproduce, analyze, test, perform and/or display publicly, prepare
 derivative works, distribute, and otherwise use matplotlib
 alone or in any derivative version, provided, however, that JDH's
 License Agreement and JDH's notice of copyright, i.e., "Copyright (c)
 2002-2011 John D. Hunter; All Rights Reserved" are retained in
 matplotlib  alone or in any derivative version prepared by
 Licensee.

 3. In the event Licensee prepares a derivative work that is based on or
 incorporates matplotlib  or any part thereof, and wants to
 make the derivative work available to others as provided herein, then
 Licensee hereby agrees to include in any such work a brief summary of
 the changes made to matplotlib.

 4. JDH is making matplotlib  available to Licensee on an "AS
 IS" basis.  JDH MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
 IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, JDH MAKES NO AND
 DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
 FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF MATPLOTLIB
 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

 5. JDH SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF MATPLOTLIB
  FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR
 LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING
 MATPLOTLIB , OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF
 THE POSSIBILITY THEREOF.

 6. This License Agreement will automatically terminate upon a material
 breach of its terms and conditions.

 7. Nothing in this License Agreement shall be deemed to create any
 relationship of agency, partnership, or joint venture between JDH and
 Licensee.  This License Agreement does not grant permission to use JDH
 trademarks or trade name in a trademark sense to endorse or promote
 products or services of Licensee, or any third party.

 8. By copying, installing or otherwise using matplotlib,
 Licensee agrees to be bound by the terms and conditions of this License
 Agreement.
Location: /home/honor675/venv/lib/python3.12/site-packages
Requires: contourpy, cycler, fonttools, kiwisolver, numpy, packaging, pillow, pyparsing, python-dateutil
Required-by:
```
## Задача 2
Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
Команда
```
npm view express
curl "$(curl -sS https://registry.npmjs.org/express/latest | jq -r .dist.tarball)" --output ./express.tgz
```
Вывод
```
express@5.2.1 | MIT | deps: 28 | versions: 289
Fast, unopinionated, minimalist web framework
https://expressjs.com/

keywords: express, framework, sinatra, web, http, rest, restful, router, app, api

dist
.tarball: https://registry.npmjs.org/express/-/express-5.2.1.tgz
.shasum: 8f21d15b6d327f92b4794ecf8cb08a72f956ac04
.integrity: sha512-hIS4idWWai69NezIdRt2xFVofaF4j+6INOpJlVOLDO8zXGpUVEVzIYk12UUi2JzjEzWL3IOAxcTubgz9Po0yXw==
.unpackedSize: 75.4 kB

dependencies:
qs: ^6.14.0, depd: ^2.0.0, etag: ^1.8.1, once: ^1.4.0, send: ^1.1.0, vary: ^1.1.2, debug: ^4.4.0, fresh: ^2.0.0, cookie: ^0.7.1, router: ^2.2.0, accepts: ^2.0.0, type-is: ^2.0.1, parseurl: ^1.3.3, statuses: ^2.0.1, encodeurl: ^2.0.0, mime-types: ^3.0.0, proxy-addr: ^2.0.7, body-parser: ^2.2.1, escape-html: ^1.0.3, http-errors: ^2.0.0, on-finished: ^2.4.1, content-type: ^1.0.5, finalhandler: ^2.1.0, range-parser: ^1.2.1
(...and 4 more.)

maintainers:
- wesleytodd <wes@wesleytodd.com>
- jonchurch <npm@jonchurch.com>
- ctcpip <c@labsector.com>
- ulisesgascon <ulisesgascondev@gmail.com>
- sheplu <jean.burellier@gmail.com>

dist-tags:
latest: 5.2.1
latest-4: 4.22.3

published 9 months ago by jonchurch <npm@jonchurch.com>
```
## Задача 3
Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.

В matplotlib_deps.dot
```
digraph matplotlib_deps {
    rankdir=LR;
    node [shape=box, style=rounded];

    matplotlib [label="matplotlib", shape=doubleoctagon, style=filled, fillcolor=lightblue];

    matplotlib -> numpy [label=">=1.21"];
    matplotlib -> pillow [label=">=8"];
    matplotlib -> contourpy [label=">=1.0.1"];
    matplotlib -> cycler;
    matplotlib -> fonttools;
    matplotlib -> kiwisolver;
    matplotlib -> packaging;
    matplotlib -> pyparsing;
    matplotlib -> python_dateutil [label=">=2.7"];
    matplotlib -> importlib_resources [style=dashed, label="Python <3.10"];

    python_dateutil -> six;
}
```
В express_deps.dot
```
digraph express_deps {
    rankdir=LR;
    node [shape=box, style=rounded];

    express [label="express", shape=doubleoctagon, style=filled, fillcolor=lightgreen];

    express -> accepts;
    express -> array_flatten;
    express -> body_parser;
    express -> content_disposition;
    express -> cookie;
    express -> debug;
    express -> depd;
    express -> encodeurl;
    express -> escape_html;
    express -> etag;
    express -> finalhandler;
    express -> fresh;
    express -> merge_descriptors;
    express -> methods;
    express -> on_finished;
    express -> parseurl;
    express -> path_to_regexp;
    express -> proxy_addr;
    express -> qs;
    express -> range_parser;
    express -> safe_buffer;
    express -> send;
    express -> serve_static;
    express -> setprototypeof;
    express -> statuses;
    express -> type_is;
    express -> utils_merge;
    express -> vary;
}
```
Команда
```
sudo apt install graphviz
nano matplotlib_deps.dot
dot -Tpng matplotlib_deps.dot -o matplotlib_deps.png
nano express_deps.dot
dot -Tpng express_deps.dot -o express_deps.png
```
<img width="704" height="707" alt="matplotlib_deps" src="https://github.com/user-attachments/assets/c26ef0ed-fe9e-42f1-88c1-3c6403bbd70f" />
<img width="411" height="2003" alt="express_deps" src="https://github.com/user-attachments/assets/891e580d-493d-4389-a50d-465300954f1f" />


## Задача 4
Следующие задачи можно решать с помощью инструментов на выбор:

Решатель задачи удовлетворения ограничениям (MiniZinc).
SAT-решатель (MiniSAT).
SMT-решатель (Z3).
Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.

Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.

В happy_ticket.mzn
```
include "all_different.mzn";

array[1..6] of var 0..9: digits;

constraint all_different(digits);

var 0..27: sum_left = digits[1] + digits[2] + digits[3];
var 0..27: sum_right = digits[4] + digits[5] + digits[6];

constraint sum_left = sum_right;

solve minimize sum_left;

output [
    "Цифры билета: \(digits[1])\(digits[2])\(digits[3])-\(digits[4])\(digits[5])\(digits[6])\n",
    "Сумма левой части: \(sum_left)\n",
    "Сумма правой части: \(sum_right)\n"
];
```
Команда
```
sudo apt install minizinc
nano happy_ticket.mzn
minizinc happy_ticket.mzn
```
Вывод
```
Цифры билета: 431-620
Сумма левой части: 8
Сумма правой части: 8
```
## Задача 5
Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.
enum PACKAGES = {root, menu, dropdown, icons};

В rootvis.mzn
```
array[PACKAGES] of set of int: versions = [
    1..1,
    1..6,
    1..6,
    1..2
];

array[PACKAGES] of var int: selected_version;

constraint forall(p in PACKAGES)(selected_version[p] in versions[p]);

constraint selected_version[root] = 1;

predicate menu_dropdown_compat(var int: m, var int: d) =
    (m = 6 /\ d = 6) \/
    (m = 5 /\ d = 5) \/
    (m = 4 /\ d = 4) \/
    (m = 3 /\ d = 3) \/
    (m = 2 /\ d = 1) \/
    (m = 1 /\ d = 1);

constraint menu_dropdown_compat(selected_version[menu], selected_version[dropdown]);

constraint selected_version[icons] in versions[icons];

solve satisfy;

output [
    "root: 1.0.0\n",
    "menu: \(selected_version[menu])\n",
    "dropdown: \(selected_version[dropdown])\n",
    "icons: \(selected_version[icons])\n"
];
```
Команда
```
nano rootvis.mzn
minizinc rootvis.mzn
```
Вывод
```
root: 1.0.0
menu: 1
dropdown: 1
icons: 1
```
## Задача 6
Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:

root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0.
foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0.
foo 1.0.0 не имеет зависимостей.
left 1.0.0 зависит от shared >=1.0.0.
right 1.0.0 зависит от shared <2.0.0.
shared 2.0.0 не имеет зависимостей.
shared 1.0.0 зависит от target ^1.0.0.
target 2.0.0 и 1.0.0 не имеют зависимостей.

В rootzav.mzn
```
enum PACKAGES = {root, foo, target, left, right, shared};

array[PACKAGES] of set of int: versions = [
    1..1,
    1..2,
    1..2,
    1..1,
    1..1,
    1..2
];

array[PACKAGES] of var int: v;

constraint forall(p in PACKAGES)(v[p] in versions[p]);

constraint v[root] = 1;
constraint v[foo] in {1, 2};
constraint v[target] = 2;

constraint (v[foo] = 2) -> (v[left] = 1 /\ v[right] = 1);
constraint (v[left] = 1) -> (v[shared] in {1, 2});
constraint (v[right] = 1) -> (v[shared] = 1);

array[1..2] of string: foo_ver    = ["1.0.0", "1.1.0"];
array[1..2] of string: target_ver = ["1.0.0", "2.0.0"];
array[1..2] of string: shared_ver = ["1.0.0", "2.0.0"];

solve satisfy;

output [
    "root: 1.0.0\n",
    "foo: " ++ foo_ver[fix(v[foo])] ++ "\n",
    "target: " ++ target_ver[fix(v[target])] ++ "\n",
    "left: 1.0.0\n",
    "right: 1.0.0\n",
    "shared: " ++ shared_ver[fix(v[shared])] ++ "\n"
];
```
Команда
```
nano rootzav.mzn
minizinc rootzav.mzn
```
Вывод
```
root: 1.0.0
foo: 1.0.0
target: 2.0.0
left: 1.0.0
right: 1.0.0
shared: 1.0.0
```
## Задача 7
Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.

В generator.py
```
packages = {
    "root": {
        "versions": ["1.0.0"],
        "dependencies": {"1.0.0": [("foo", "^1.0.0"), ("target", "^2.0.0")]}
    },
    "foo": {
        "versions": ["1.0.0", "1.1.0"],
        "dependencies": {
            "1.0.0": [],
            "1.1.0": [("left", "^1.0.0"), ("right", "^1.0.0")]
        }
    },
    "target": {
        "versions": ["1.0.0", "2.0.0"],
        "dependencies": {"1.0.0": [], "2.0.0": []}
    },
    "left": {
        "versions": ["1.0.0"],
        "dependencies": {"1.0.0": [("shared", ">=1.0.0")]}
    },
    "right": {
        "versions": ["1.0.0"],
        "dependencies": {"1.0.0": [("shared", "<2.0.0")]}
    },
    "shared": {
        "versions": ["1.0.0", "2.0.0"],
        "dependencies": {
            "1.0.0": [("target", "^1.0.0")],
            "2.0.0": []
        }
    }
}

def parse_version(v):
    return tuple(int(x) for x in v.split("."))

def version_satisfies(version_str, constraint_str):
    v = parse_version(version_str)
    if constraint_str.startswith("^"):
        base = parse_version(constraint_str[1:])
        return base <= v < (base[0] + 1, 0, 0)
    if constraint_str.startswith(">="):
        return v >= parse_version(constraint_str[2:])
    if constraint_str.startswith("<="):
        return v <= parse_version(constraint_str[2:])
    if constraint_str.startswith("<"):
        return v < parse_version(constraint_str[1:])
    if constraint_str.startswith(">"):
        return v > parse_version(constraint_str[1:])
    if constraint_str.startswith("="):
        return v == parse_version(constraint_str[1:])
    return False

def generate_mzn(packages):
    lines = ["% Авто-сгенерированная модель MiniZinc", ""]
    pkg_names = list(packages.keys())

    lines.append("enum PACKAGES = {" + ", ".join(pkg_names) + "};")
    lines.append("")
    lines.append("array[PACKAGES] of set of int: versions = [")
    for name in pkg_names:
        n = len(packages[name]["versions"])
        lines.append(f"    0..{n},")
    lines.append("];")
    lines.append("")
    lines.append("array[PACKAGES] of var int: v;")
    lines.append("constraint forall(p in PACKAGES)(v[p] in versions[p]);")
    lines.append("")
    lines.append("% root всегда установлен в версии 1.0.0 (индекс 1)")
    lines.append("constraint v[root] = 1;")
    lines.append("")

    for name, info in packages.items():
        for idx, ver_str in enumerate(info["versions"], start=1):
            for dep_name, constraint_str in info["dependencies"].get(ver_str, []):
                allowed = [
                    dep_idx
                    for dep_idx, dep_ver in enumerate(packages[dep_name]["versions"], start=1)
                    if version_satisfies(dep_ver, constraint_str)
                ]
                if not allowed:
                    lines.append(f"constraint v[{name}] != {idx};")
                else:
                    allowed_str = " \\/ ".join(f"v[{dep_name}] = {i}" for i in allowed)
                    lines.append(f"constraint (v[{name}] = {idx}) -> ({allowed_str});")

    lines.append("")
    lines.append("solve satisfy;")
    lines.append("")
    lines.append("output [")
    for name in pkg_names:
        lines.append(f'    "{name}: \\(v[{name}])\\n",')
    lines.append("];")
    return "\n".join(lines)

with open("package_deps.mzn", "w") as f:
    f.write(generate_mzn(packages))
print("Сгенерировано: package_deps.mzn")
```
Команда
```
python3 generator.py
minizinc package_deps.mzn
```
Вывод
```
Сгенерировано: package_deps.mzn
root: 1
foo: 1
target: 2
left: 0
right: 0
shared: 0
```
