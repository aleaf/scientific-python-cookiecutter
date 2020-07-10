{% set section_separator = "=" * cookiecutter.project_name | length -%}
{{ section_separator }}
{{ cookiecutter.project_name }}
{{ section_separator }}

[![Build Status](https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}) [![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/branch/develop/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }})

{{ cookiecutter.project_short_description}}

* Free software: 3-clause BSD license
* Documentation: (COMING SOON!) https://{{ cookiecutter.github_username}}.github.io/{{ cookiecutter.repo_name }}.

Features
--------

* TODO
