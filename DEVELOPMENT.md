Development
===========

This document is intended to describe the structure of the project, how to 
perform various development tasks, and also link to references that directed
the setup.

I started this structure based on information found here:

  http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/

Code goes in ``codewatch/``. Tests go in ``test``. 

Run tests with the command ``python setup.py test``.


## Design

We have a:
  data type -- coverage data or rule sets



When a build runs, all configured data gets stored as a note attached to the
given sha.

We also post diff information to the commit. If the commit is a PR, then we
post a diff between the commit and the target. These are posted as markdown
comments on github.

We store a browseable website (javascript?) of all historical data. This is on
a configurable subdirectory of the gh-pages branch. Only certain branches are
stored in this website, we want to focus on active branches, tags, and pull
requests.

The tool allows pulling reports out for a given sha.

Phase 1: Arbitrary data stored.
Phase 1a: invoked by travis (using setup tools)
Phase 2: coverage data stored. 
Phase 3: diff generated on stdout
Phase 4: rule data stored and diffed on stdout (probably pylint)
Phase 5: diff info posted to commits
Phase 6: diff info posted to pull requests
Phase 7: pass/fail outputted based on diff and thresholding info
Phase 8: PR statuses updated with pass/fail 
Phase 9: coverage and rule data moved into plugins
Phase 10: diff info published to PRs as well-formatted comments
Phase 11: browseable website published to gh-pages
Phase 12: maven project publishing info
Phase 13: "post" functionality pluginified
Phase 13a: stash support added
Phase 14: website functionality pluginified
Phase 14a: static ftp server added
Phase 15: Gradle support
Phase 16: gulp support
Phase 17: rake support
