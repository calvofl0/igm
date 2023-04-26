#!/usr/bin/env python
# Copyright (C) 2021-2022 Guillaume Jouvet <guillaume.jouvet@unil.ch>
# Published under the GNU GPL (Version 3)

from setuptools import setup, find_packages
import versioneer

name="igm"
version=versioneer.get_version()

setup(
    name=name,
    version=version,
    cmdclass=versioneer.get_cmdclass(),
    author="Guillaume Jouvet",
    author_email="guillaume.jouvet@unil.ch",
    description="The Instructed Glacier Model",
    url="https://github.com/jouvetg/igm",
    license="gpl-3.0",
    package_dir={"": "src"},
    command_options={
        'build_sphinx': {
            'project': ('setup.py', ''.join(name)),
            'version': ('setup.py', ''.join(version)),
            'source_dir': ('setup.py', 'docs/source'),
            'build_dir': ('setup.py', 'docs/_build')}}
)
