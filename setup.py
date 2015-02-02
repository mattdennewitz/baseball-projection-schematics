#!/usr/bin/env python

import os
from setuptools import setup, find_packages

from pip.req import parse_requirements


reqs_txt = os.path.join(os.path.dirname(__file__), 'requirements.txt')
pip_reqs = [unicode(obj.req) for obj in parse_requirements(reqs_txt)]

setup(
    name = 'baseball-projection-schematics',
    version = '0.1.0',
    description = 'Translates projection data into a unified schema',
    author = 'Matt Dennewitz',
    author_email = 'mattdennewitz@gmail.com',
    url = 'https://github.com/mattdennewitz/baseball-projection-schematics',

    include_package_data = True,

    install_requires = pip_reqs,

    packages = find_packages(),

    scripts = [
        'scripts/bb-generate-schematic',
        'scripts/bb-process-projections',
    ],
)
