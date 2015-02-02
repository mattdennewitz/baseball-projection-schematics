#!/usr/bin/env python

from __future__ import unicode_literals
import codecs
import json
import optparse
import os
import pprint
import re
import sys

import click

from schematics.exceptions import ModelValidationError

import unicodecsv as csv

from projnorm import configreader
from projnorm.models import ProjectionSchematic


space_re = re.compile(r'\s\s+')

def clean_text(value):
    if value:
        return space_re.sub(' ', value).strip()
    return value


def clean_value(value, default=None):
    if not value:
        if default:
            return default
        return value
    if isinstance(value, basestring):
        value = clean_text(value)
    return float(value)


def process(schematic, data_fp):
    "Processes a batting or pitching projection"

    data = csv.DictReader(codecs.open(data_fp.name, 'rb', 'utf-8'),
                          encoding='utf-8-sig')

    for row in data:
        projected_line = {}

        # build player information
        if schematic.player.name.full is not None:
            player_name = row[schematic.player.name.full]
        else:
            player_name = '%s, %s' % (row[schematic.player.name.last],
                                      row[schematic.player.name.first])

        # get player roles, flatten into comma-separated string
        roles = []
        if schematic.player.roles:
            for key in schematic.player.roles:
                roles_ = row[key]
                if roles_:
                    split_roles = roles_.split(',')
                    for split_role in split_roles:
                        if not split_role in roles:
                            roles.append(split_role)

        # add player information
        projected_line.update(
            name = player_name,
            age = row.get(schematic.player.age),
            bats = row.get(schematic.player.hands.bats),
            throws = row.get(schematic.player.hands.throws),
            league = row.get(schematic.player.league),
            roles = ','.join(roles)
        )

        # build player keys
        for key in schematic.player.ids:
            column_name = schematic.player.ids[key]
            value = None
            if column_name is not None:
                value = row.get(column_name)
            projected_line[key] = value

        # build components
        for key in schematic.components:
            column_name = schematic.components[key]
            value = None
            if column_name is not None:
                value = row.get(column_name)
            projected_line[key] = value

        yield projected_line


@click.command()
@click.option('-s', '--schematic', 'schematic_fp', type=click.File('rb'),
              help='Path to JSON schematic', required=True)
@click.option('-t', '--type', 'projection_type',
              type=click.Choice(('batting', 'pitching', )), required=True)
@click.option('-i', '--input', 'input_fp', type=click.File('rb'),
              required=True)
@click.option('-c', '--config', 'config_fp', type=click.File('rb'),
              required=True)
@click.argument('destination', type=click.File('w'), required=True)
def process_projections(schematic_fp, projection_type, input_fp,
                        config_fp, destination):
    # read config
    config = configreader.read_from_file(config_fp)

    # load schematic
    schematic = ProjectionSchematic(json.load(schematic_fp))

    # process input
    projections = process(schematic[projection_type], input_fp)

    # start off with basic player information
    columns = ['name', 'age', 'bats', 'throws', 'league', 'roles']
    # add player id keys
    columns.extend( sorted(schematic[projection_type].player.ids.keys()) )
    # add components
    columns.extend( config.components[projection_type] )

    # write header row and re-formatted projections
    writer = csv.writer(destination)
    writer.writerow(columns)

    for line in projections:
        writer.writerow([
            clean_text(line[key])
            for key
            in columns
        ])


if __name__ == '__main__':
    process_projections()
