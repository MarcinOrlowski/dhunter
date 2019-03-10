 [![dhunter logo](img/logo.png)](https://github.com/MarcinOrlowski/dhunter)
 ---

 [![PyPI version](https://badge.fury.io/py/dhunter.svg)](https://badge.fury.io/py/dhunter)
 [![CodeFactor Code Rating](https://www.codefactor.io/repository/github/MarcinOrlowski/dhunter/badge?style=flat-square)](https://www.codefactor.io/repository/github/marcinorlowski/mp3voicestamp)
 [![Codacy Badge](https://api.codacy.com/project/badge/Grade/db7e95272e1a44889920bded7620c8b3)](https://www.codacy.com/app/MarcinOrlowski/dhunter?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=MarcinOrlowski/dhunter&amp;utm_campaign=Badge_Grade)
 [![codebeat badge](https://codebeat.co/badges/1ff9f5ad-3e95-4ffb-94d1-08eb2f360987)](https://codebeat.co/projects/github-com-marcinorlowski-dhunter-master)
 [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MarcinOrlowski/dhunter.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MarcinOrlowski/dhunter/context:python)
 [![Reviewed by Hound](https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg)](https://houndci.com)

## Table of contents ##

 * [Introduction](#introduction)
 * [Features](#features)
 * [Configuration and usage](docs/usage.md)
 * [Requirements and installation](docs/install.md)
 * [Bugs reports and contributions](docs/contribute.md)
 * [Credits and license](#credits-and-license)
 * [What's new?](docs/CHANGES.md)

## Introduction ##

 dhunter (pronounced The Hunter) is [d]uplicate [hunter] utility, designed
 to help scanning and processing large sets of files. Uses content based
 file duplicates matching and smart caching for faster directory scanning,
 data changes detection and processing.

## Features ##

 * Content based file matching
 * Designed to work with lot of data:
   * caches folder scaning results for quick reuse
   * directory scanning can be aborted and **resumed** at any moment
 * Smart content filters:
   * Ignores zero length files
   * Ignores folders like `.git`, `.cvs`, `.svn`
   * Supports user configurable file size filter (min and/or max)

## Credits and license ##

 * Written and copyrighted ©2018-2019 by Marcin Orlowski
 * dhunter is open-sourced software licensed under the MIT license
