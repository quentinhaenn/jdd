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
    - [Preriquisites](#preriquisites)
    - [Generate Everything](#generate-everything)
      - [Example](#example)
    - [Make stats](#make-stats)
    - [Make badges](#make-badges)
    - [Make signing pages](#make-signing-pages)
    - [Make QR Codes](#make-qr-codes)
    - [Combining Commands](#combining-commands)
      - [Example](#example-1)
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
python3.7 -m pip install setuptools pandas seaborn matplotlib os colorama openpyxl pytest qrcode
```

This will install all dependencies for you.

>[!Note]
>You can modify the python version you're using e.g. : python3.10 or python 3.11.

>[!Note]
>This will do the magic whether on Linux or Windows. You also can use python alone on windows is set on PATH variable.

## Tests

To ensure all is set up correctly, please run :

```bash
pytest
```

If every test is passed, then everything is set up !

## How to

This section includes most of useful commands to help you manage participants in MIMME JDDs. Refer to the correct section for what you need.

### Preriquisites

In order to generate all files you need with this module, there are little prerequisites especially concerning input files and where you put them. You must use this file tree organization, considering you have a list of all attendees in a file named `participants-2024.xlsx` :

```bash
jdd/
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING
├── LICENCE
├── out/ #<-- where the generated files will go.
│   └── tex/ #<-- is where generated tex files will go.
├── README.md
└── src/ #<-- where all code is written
    ├── jdd/
    │   ├── main.py #<-- does all the magic
    │   │   
    │   └── tools/ #<-- where all intelligent code is.
    ├── resource/ #<-- where you put your xlsx file, and where csv files will go.
    │   └── participants-2024.xlsx #<-- your input file
    └── tests/ #<-- where tests are performed
```

>[!Important]
>Moreover, be sure your xlsx file strictly follows the structure of the `Participants JDD sample.xlsx` sample provided with this archive. In case not, this script will not perform anything and will crash.

Now you may have everything set up to generated everything.

### Generate Everything

To generate every single file that script is capable to, simply use :

```bash
python<version> src/jdd/main.py <name_of_excel_file>
```

This will generate `noms_complets.csv`, `noms_ensma.csv`, `noms_up.csv`, `badges.tex`, `list_ensma.tex`, `list_up.tex`, `stats.txt`, `Stats Participants JDD.png` and `Stats presentations JDD.png` files.

>[!Note]
> All `.csv` files are located in `src/resource` dir because they are reused by scripts as resources.
> All other files created are located in `out/` directory.

#### Example

Considering you have python 3.7 installed and `participants-2024.xlsx` as input file :

```bash
python3.7 src/jdd/main.py participants-2024.xlsx
```

### Make stats

This is used to make some stats about JDDs participants :

- Number of attendees
- Number of expected posters
- Number of expected presentations
- Stats on each laboratory represented

Use the following code line in command prompt to launch it :

```bash
python<version> src/jdd/main.py <name_of_excel_file> -ms
```

Or alternatively :

```bash
python<version> src/jdd/main.py <name_of_excel_file> --make-stats
```

### Make badges

To make the `badges.tex` file used to automatically make badges with LaTeX, use the following prompt :

```bash
python<version> src/jdd/main.py <name_of_excel_file> -b
```

Or alternatively :

```bash
python<version> src/jdd/main.py <name_of_excel_file> --badges
```

### Make signing pages

To make the `list_ensma.tex` and `list_up.tex` files used to automatically make signing lists with LaTeX, use the following prompt :

```bash
python<version> src/jdd/main.py <name_of_excel_file> -s
```

Or alternatively :

```bash
python<version> src/jdd/main.py <name_of_excel_file> --signing-lists
```

### Make QR Codes

Considering you have several documents accessible via url links, you can make your QR codes using this module.

First, you have to invoke the proper command using the following command line :

```bash
python<version> src/jdd/main.py -qr
```

Then the console will ask you to type the url(s) you want to transform into QR codes as follow :

<p align="center">
  <img width="600" src="./qrcodes.svg">
</p>

Have to run with this command for svg and asciinema rec :

```bash
asciinema rec <name>
```

then 
```bash
npx -p svg-term-cli svg-term --cast=ltJiXfQ6AboJfODHnnAs6e9RF --out qrcodes.svg --window
```

### Combining Commands

If you want to combine two commands, use the proper options to do so.

#### Example

You want to generate badges and signing lists but no stats :

```bash
python<version> src/jdd/main.py <name_of_excel_file> -b -s
```

Or alternatively :

```bash
python<version> src/jdd/main.py <name_of_excel_file> --badges --signing-lists
```

## Next steps

The next steps for this project are :

- [x] Finish README
- [x] Color prints
- [x] Make a stat file with all stats included
- [x] Make an out directory for all files created
- [x] Create the QR code functionality -> [dedicated issue](https://github.com/quentinhaenn/jdd/issues/7)
- [ ] Create the auto-order functionality -> [dedicated issue](https://github.com/quentinhaenn/jdd/issues/8)
- [ ] Make all unit tests
- [x] Setup CI/CD
- [ ] Deploy
- [ ] Show examples
- [ ] Make it available on PyPi

You also can follow the project's progression on [issue tracker page](https://github.com/quentinhaenn/jdd/issues).

## Contributing

There are many ways to contribute to this. See `CONTRIBUTING.md` file for more informations.

## Authors

- [Haenn Quentin](https://github.com/quentinhaenn) : [Contact me](mailto:quentin.haenn@ensma.fr) :mailbox: