#!/usr/bin/env python

"""Generates a configurable projection schema
"""

from __future__ import unicode_literals
import os
import sys

import click

import json

import schematics

from jinja2 import FileSystemLoader, Environment, Template
from jinja2.ext import with_

from projnorm import settings, configreader


@click.command()
@click.option('-t', '--template', type=click.Path(exists=True),
              required=True, help='Path to JSON schematic template')
@click.option('-c', '--config', 'config_fp', type=click.File('rb'),
              required=True, help='Path to schematic configuration')
@click.option('--sort-keys/--no-sort-keys', default=True,
              help='Sort JSON keys? (Recommended)')
@click.option('-i', '--indent', type=click.INT, default=4,
              help='JSON output indentation level')
@click.argument('destination', type=click.File('w'), required=True)
def generate_schema(template, config_fp, destination, sort_keys, indent):
    """Generates a schema from given template and configuration.
    """

    config = configreader.read_from_file(config_fp)

    template_base = os.path.dirname(os.path.realpath(template))
    template_name = template.split(os.sep)[-1]

    # read template
    jinja_env = Environment(extensions=[with_],
                            loader=FileSystemLoader(template_base))
    template = jinja_env.get_template(template_name)

    # render
    rendered = template.render({
        'config': config,
        'id_systems': settings.ID_SYSTEMS,
    })

    # clean, write to final destination
    json.dump(json.loads(rendered),
              destination,
              indent=indent,
              sort_keys=sort_keys)


if __name__ == '__main__':
    generate_schema()
