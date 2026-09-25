# Практическое занятие №1. Введение, основы работы в командной строке

Юдин Д.А.

Научиться выполнять простые действия с файлами и каталогами в Linux из командной строки. Сравнить работу в командной строке Windows и Linux.

## Задача 1

Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).

Команда
```
grep -o '^[^:]*' /etc/passwd | LC_ALL=C sort
```
Вывод
```
bin
cron
daemon
ftp
games
guest
halt
lp
mail
news
nobody
ntp
root
shutdown
sshd
sync
uucp
```
## Задача 2

Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:

```
[root@localhost etc]# cat /etc/protocols ...
142 rohc
141 wesp
140 shim6
139 hip
138 manet
```

Команда
```
awk '!/^#/ && NF >= 2 {print $2, $1}' /etc/protocols | sort -k1,1nr | head -n5
```
Вывод
```
262 mptcp
143 ethernet
142 rohc
141 wesp
140 shim6
```

## Задача 3

Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):

```
[root@localhost ~]# ./banner "Hello from RTU MIREA!"
+-----------------------+
| Hello from RTU MIREA! |
+-----------------------+
```

Перед отправкой решения проверьте его в ShellCheck на предупреждения.

В banner
```
#!/usr/bin/env bash
set -euo pipefail

if (( $# == 0 )); then
  echo "Usage: $0 text" >&2
  exit 1
fi

text="$*"
len=$(( ${#text} + 2 ))
border=$(printf '%*s' "$len" '' | tr ' ' '-')

printf '+%s+\n| %s |\n+%s+\n' "$border" "$text" "$border"
```
Команда
```
nano banner
chmod +x banner
./banner "Hello from RTU MIREA!"
```
Вывод
```
+-----------------------+
| Hello from RTU MIREA! |
+-----------------------+
```

## Задача 4

Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).

Пример для hello.c:

```
h hello include int main n printf return stdio void world
```

В banner
```
#!/usr/bin/env bash
set -euo pipefail

if (( $# != 1 )); then
  echo "Usage: $0 <file>" >&2
  exit 1
fi

grep -oE '[A-Za-z_$][A-Za-z0-9_$]*' -- "$1" | sort -u | paste -sd ' ' -
```
Команда
```
nano banner
chmod +x banner
./banner hello.c
```
Вывод
```
h hello include int main n printf return stdio void world
```

## Задача 5

Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).

Например, пусть программа называется reg:

```
./reg banner
```

В banner
```
echo "Hello world"
```
В reg
```
#!/usr/bin/env bash
set -euo pipefail

if (( $# != 1 )); then
  echo "Usage: $0 <program>" >&2
  exit 1
fi

prog="$1"

if [[ ! -f "$prog" ]]; then
  echo "Not a file: $prog" >&2
  exit 1
fi

sudo install -m 0755 -- "$prog" /usr/local/bin/
```
Команда
```
nano banner
nano reg
chmod +x reg
./reg banner
```

В результате для banner задаются правильные права доступа и сам banner копируется в /usr/local/bin.

## Задача 6

Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.

В banner
```
#!/usr/bin/env bash
set -euo pipefail

if (( $# == 0 )); then
  echo "Usage: $0 <file-or-dir>..." >&2
  exit 1
fi

check_file() {
  local f="$1"
  local first
  first=$(head -n 1 -- "$f" 2>/dev/null || true)

  case "$f" in
    *.c|*.js)
      if grep -Eq '^[[:space:]]*(//|/\*)' <<< "$first"; then
        echo "$f: comment"
      else
        echo "$f: no comment"
      fi
      ;;
    *.py)
      if grep -Eq '^[[:space:]]*#' <<< "$first"; then
        echo "$f: comment"
      else
        echo "$f: no comment"
      fi
      ;;
  esac
}

for arg in "$@"; do
  if [[ -d "$arg" ]]; then
    while IFS= read -r -d '' f; do
      check_file "$f"
    done < <(find "$arg" -type f \( -name '*.c' -o -name '*.js' -o -name '*.py' \) -print0)
  else
    check_file "$arg"
  fi
done
```
Команда
```
nano banner
chmod +x banner
./banner p.py
```
Вывод
```
p.py: no comment
```

## Задача 7

Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).

В banner
```
#!/usr/bin/env bash
set -euo pipefail

if (( $# != 1 )); then
  echo "Usage: $0 <directory>" >&2
  exit 1
fi

dir="$1"

find "$dir" -type f -print0 |
  xargs -0 -r sha256sum |
  sort -k1,1 |
  awk '
    {
      hash=$1
      $1=""
      sub(/^ +/, "")
      file=$0

      if (hash == prev) {
        if (!shown) {
          print prev_file
          shown=1
        }
        print file
      } else {
        shown=0
      }

      prev=hash
      prev_file=file
    }'
```
Команда
```
nano banner
chmod +x banner
./banner /etc
```
Вывод
```
find: ‘/etc/credstore.encrypted’: Permission denied
find: ‘/etc/credstore’: Permission denied
find: ‘/etc/ssl/private’: Permission denied
find: ‘/etc/polkit-1/rules.d’: Permission denied
sha256sum: /etc/sudoers: Permission denied
sha256sum: /etc/gshadow: Permission denied
sha256sum: /etc/gshadow-: Permission denied
sha256sum: /etc/.pwd.lock: Permission denied
sha256sum: /etc/landscape/client.conf: Permission denied
sha256sum: /etc/sudoers.d/README: Permission denied
sha256sum: /etc/shadow: Permission denied
sha256sum: /etc/security/opasswd: Permission denied
sha256sum: /etc/shadow-: Permission denied
/etc/subgid
/etc/subuid
/etc/cloud/templates/ntp.conf.almalinux.tmpl
/etc/cloud/templates/ntp.conf.cloudlinux.tmpl
/etc/cloud/templates/ntp.conf.photon.tmpl
/etc/cloud/templates/ntp.conf.rocky.tmpl
/etc/cloud/templates/chrony.conf.fedora.tmpl
/etc/cloud/templates/chrony.conf.photon.tmpl
/etc/cron.d/.placeholder
/etc/cron.daily/.placeholder
/etc/cron.hourly/.placeholder
/etc/cron.monthly/.placeholder
/etc/cron.weekly/.placeholder
/etc/cron.yearly/.placeholder
/etc/magic
/etc/magic.mime
/etc/console-setup/Uni2-Fixed16.psf.gz
/etc/console-setup/cached_Uni2-Fixed16.psf.gz
/etc/cloud/templates/chrony.conf.opensuse-leap.tmpl
/etc/cloud/templates/chrony.conf.opensuse-microos.tmpl
/etc/cloud/templates/chrony.conf.opensuse-tumbleweed.tmpl
/etc/cloud/templates/chrony.conf.opensuse.tmpl
/etc/cloud/templates/chrony.conf.sle-micro.tmpl
/etc/cloud/templates/chrony.conf.sle_hpc.tmpl
/etc/cloud/templates/chrony.conf.sles.tmpl
/etc/apparmor.d/local/lsb_release
/etc/apparmor.d/local/nvidia_modprobe
/etc/apparmor.d/local/ubuntu_pro_apt_news
/etc/apparmor.d/local/ubuntu_pro_esm_cache
/etc/apparmor.d/local/usr.bin.man
/etc/apparmor.d/local/usr.lib.snapd.snap-confine.real
/etc/apparmor.d/local/usr.sbin.rsyslogd
/etc/cloud/cloud-init.disabled
/etc/newt/palette.original
/etc/sensors.d/.placeholder
/etc/subgid-
/etc/subuid-
/etc/cloud/templates/ntp.conf.opensuse.tmpl
/etc/cloud/templates/ntp.conf.sles.tmpl
/etc/cloud/templates/chrony.conf.almalinux.tmpl
/etc/cloud/templates/chrony.conf.centos.tmpl
/etc/cloud/templates/chrony.conf.cloudlinux.tmpl
/etc/cloud/templates/chrony.conf.rhel.tmpl
/etc/cloud/templates/chrony.conf.rocky.tmpl
```

## Задача 8

Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.

В banner
```
#!/usr/bin/env bash
set -euo pipefail

if (( $# != 3 )); then
  echo "Usage: $0 <directory> <extension> <archive.tar>" >&2
  exit 1
fi

dir="$1"
ext="${2#.}"
archive="$3"

find "$dir" -type f -name "*.$ext" -print0 |
  tar --null -T - -cf "$archive"
```
Команда
```
nano banner
chmod +x banner
./banner /home/user/txt txt text_files.tar
```

## Задача 9

Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.

В banner
```
#!/usr/bin/env bash
set -euo pipefail

if (( $# != 2 )); then
  echo "Usage: $0 <input> <output>" >&2
  exit 1
fi

sed 's/    /\t/g' -- "$1" > "$2"
```
Команда
```
nano banner
chmod +x banner
./banner input.txt output.txt
```

## Задача 10

Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром. 

В banner
```
#!/usr/bin/env bash
set -euo pipefail

if (( $# != 1 )); then
  echo "Usage: $0 <directory>" >&2
  exit 1
fi

find "$1" -maxdepth 1 -type f -empty -printf '%f\n'
```
Команда
```
nano banner
chmod +x banner
./banner /etc
```
Вывод
```
.pwd.lock
subuid-
subgid-
```
