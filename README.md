# MIMME JDD HELP PACKAGE

This package is made to help MIMME's JDDs organization.

## Table of Content

- [MIMME JDD HELP PACKAGE](#mimme-jdd-help-package)
  - [Table of Content](#table-of-content)
  - [Quick Overview](#quick-overview)
  - [Requirements](#requirements)
    - [Installing Python](#installing-python)
  - [Installation](#installation)
  - [How to](#how-to)
    - [Make stats](#make-stats)
    - [Make badges](#make-badges)
    - [Make signing pages](#make-signing-pages)
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
- `build` up-to-date
- `Pandas` up-to-date
- `qr` up-to-date
- `click` up-to-date
- A complete and functional LaTeX distribution ([TeXLive](https://tug.org/texlive/acquire-netinstall.html) for instance)

You don't need to install them manually, `pip` will do it for you when installing, but `Python` and `pip` are mandatory to do so.

### Installing Python

- On Windows : go on [python Windows Download page](https://www.python.org/downloads/windows/) and download latest release
- On Linux (Ubuntu/Debian): simply run `sudo apt install python3`. You can also run `apt-get`.
- On MacOS : go on [python MacOs Download Page](https://www.python.org/downloads/macos/) and download latest release

## Installation

Download  `.zip` archive from github(insert link) or clone the repository on your machine.

In further release we plan to make it available on PyPi projects to make it available via pip installation. See [Next Steps](#next-steps) for more informations

## How to

This section includes most of useful commands to help you manage participants in MIMME JDDs. Refer to the correct section for what you need.

### Make stats

This is used to make some stats about JDDs participants :

- Number of attendees
- Number of expected posters
- Number of expected presentations
- Stats on each laboratory represented

TODO Insert CLI.

### Make badges

TODO

### Make signing pages

TODO

## Next steps

The next steps for this project are :

- [ ] Finish README
- [ ] Make all unit tests
- [ ] Setup CI/CD
- [ ] Deploy
- [ ] Show examples
- [ ] Make it available on PyPi

## Contributing

There are many ways to contribute to this. See `CONTRIBUTING.md` file for mare informations.
## Authors

- [Haenn Quentin](https://github.com/quentinhaenn) mail : quentin.haenn@ensma.fr