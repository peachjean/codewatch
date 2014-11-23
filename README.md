codewatch
=========

[![Build Status](https://travis-ci.org/peachjean/codewatch.svg)](https://travis-ci.org/peachjean/codewatch)
[![Documentation Status](https://readthedocs.org/projects/codewatch/badge/?version=latest)](https://readthedocs.org/projects/codewatch/?badge=latest)

A utility for tracking code analysis metrics directly in the git repository.

The basic goal here is to provide github-based projects the ability to track code quality metrics over time without using any service other than github and a CI. As far as any CI integration will be built into this product, my initial focus will be [travis](https://travis-ci.org/) but I see no reason that we would be locked into that.

This is still a work in progress. The general plan is to build this from 5 building blocks:

1. Utility for accessing git notes and working out which to use, most recent comparison point, etc. The basic "store tracked data in the repository" machinery.
2. Configuration Utility -- what configurations, etc are we using. Parsing ``.codewatch.yml`` and making its contents available.
3. Abstraction for metric types -- provides resource parsing, diff capabilities, and readable posting formats. Starting with:
  1. Coverage
  2. Rule Sets
4. Abstraction for the hosting API (discoverable, a discoverable endpoint based on ``.git/config``, overrideable in ``.codewatch.yml``. Starting with github, could eventually potentialy support:
  1. Stash
  2. Bitbucket
  3. Gitlab
5. Build Tool Plugins
  1. SetupTools
  2. Gulp
  3. Maven
  4. Rake
  5. Gradle


The tool is written in python, but is intended to be used across languages.
