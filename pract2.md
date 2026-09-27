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

## Задача 5
Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.

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

## Задача 7
Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.
