# MIMME JDD HELP PACKAGE

This package is made to help MIMME's JDDs organization.

## Table of Content

- [MIMME JDD HELP PACKAGE](#mimme-jdd-help-package)
  - [Table of Content](#table-of-content)
  - [Quick Overview](#quick-overview)
  - [Requirements](#requirements)
    - [Installing Python](#installing-python)
  - [Installation](#installation)
    - [Manual installation of dependencies](#manual-installation-of-dependencies)
  - [Tests](#tests)
  - [How to](#how-to)
    - [Generate Everything](#generate-everything)
    - [Make stats](#make-stats)
    - [Make badges](#make-badges)
    - [Make signing pages](#make-signing-pages)
    - [Combining Commands](#combining-commands)
  - [Next steps](#next-steps)
  - [Contributing](#contributing)
  - [Authors](#authors)

## Quick Overview

You'll have to deal with hundreds participants and same amount of badges, presentations and posters, you definitely don't want to deals with by hand. This package is made for you !

You'll be able to automatically build badges and signing pages relative to the list of participants provided by MIMME secretary, make stats and even make a random passage order for the presentations !

Functionalities :

1. Auto badges
2. Auto signing pages
3. Auto order for presentations
4. Auto QR-codes for important files (book of abstract and conf program)
5. Auto stats

## Requirements

What's needed to make this work.

- `Python` >= 3.7
- `Pandas` up-to-date
- `openpyxl` up-to-date
- `matplotlib` up-to-date
- `qr` up-to-date
- A complete and functional LaTeX distribution ([TeXLive](https://tug.org/texlive/acquire-netinstall.html) for instance)

You don't need to install them manually, `pip` will do it for you when installing, but `Python` and `pip` are mandatory to do so.

### Installing Python

- On Windows : go on [python Windows Download page](https://www.python.org/downloads/windows/) and download latest release
- On Linux (Ubuntu/Debian): simply run `sudo apt install python3`. You can also run `apt-get`.
- On MacOS : go on [python MacOs Download Page](https://www.python.org/downloads/macos/) and download latest release

## Installation

Download  `.zip` archive from github(insert link) or clone the repository on your machine.

In further release we plan to make it available on PyPi projects to make it available via pip installation. See [Next Steps](#next-steps) for more informations

### Manual installation of dependencies

If you do not use `pip` and PyPi repository to get this package, please remember that you do need to manually install every dependency needed. Use the following code in command prompt :

```bash
python3.7 -m pip install setuptools pandas seaborn matplotlib os colorama openpyxl pytest
```

This will install all dependencies for you.

> Note : You can modify the python version you're using e.g. : python3.10 or python 3.11.

> Note : This will do the magic whether on Linux or Windows. You also can use python alone on windows is set on PATH variable.

## Tests

To ensure all is set up correctly, please run :

```bash
pytest
```

If every test is passed, then everything is set up !

## How to

This section includes most of useful commands to help you manage participants in MIMME JDDs. Refer to the correct section for what you need.

### Generate Everything

To generate every single file that script is capable to, simply use :

```bash
python3.7 src/jdd/main.py <name_of_excel_file>
```

This will generate `noms_complets.csv`, `noms_ensma.csv`, `noms_up.csv`, `badges.tex`, `list_ensma.tex`, `list_up.tex`, `stats.txt`, `Stats Participants JDD.png` and `Stats presentations JDD.png` files.

> Note : All `.csv` files are located in `src/resource` dir because they are reused by scripts as resources.

> Note : All other files created are located in `out/` directory.

### Make stats

This is used to make some stats about JDDs participants :

- Number of attendees
- Number of expected posters
- Number of expected presentations
- Stats on each laboratory represented

Use the following code line in command prompt to launch it :

```bash
python3.7 src/jdd/main.py <name_of_excel_file> -ms
```

Or alternatively :

```bash
python3.7 src/jdd/main.py <name_of_excel_file> --make-stats
```

### Make badges

To make the `badges.tex` file used to automatically make badges with LaTeX, use the following prompt :

```bash
python3.7 src/jdd/main.py <name_of_excel_file> -b
```

Or alternatively :

```bash
python3.7 src/jdd/main.py <name_of_excel_file> --badges
```

### Make signing pages

To make the `list_ensma.tex` and `list_up.tex` files used to automatically make signing lists with LaTeX, use the following prompt :

```bash
python3.7 src/jdd/main.py <name_of_excel_file> -s
```

Or alternatively :

```bash
python3.7 src/jdd/main.py <name_of_excel_file> --signing-lists
```

### Combining Commands

If you want to combine two commands, use the proper options to do so.

E.G : you want to generate badges and signing lists but no stats :

```bash
python3.7 src/jdd/main.py <name_of_excel_file> -b -s
```

Or alternatively :

```bash
python3.7 src/jdd/main.py <name_of_excel_file> --badges --signing-lists
```

## Next steps

The next steps for this project are :

- [x] Finish README
- [x] Color prints
- [x] Make a stat file with all stats included
- [x] Make an out directory for all files created
- [ ] Create the QR code functionality
- [ ] Create the auto-order functionality 
- [ ] Make all unit tests
- [x] Setup CI/CD
- [ ] Deploy
- [ ] Show examples
- [ ] Make it available on PyPi

You also can follow the project's progression on [issue tracker page](https://github.com/quentinhaenn/jdd/issues).

## Contributing

There are many ways to contribute to this. See `CONTRIBUTING.md` file for more informations.

## Authors

- [Haenn Quentin](https://github.com/quentinhaenn) mail : quentin.haenn@ensma.fr