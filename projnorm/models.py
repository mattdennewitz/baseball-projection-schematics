from __future__ import unicode_literals

from schematics import models, types


#
# configuration layout
#

class ConfigComponentMap(models.Model):
    batting = types.compound.ListType(types.StringType())
    pitching = types.compound.ListType(types.StringType())


class ConfigSchematic(models.Model):
    "Schematic for schema generation configuration"

    components = types.compound.ModelType(ConfigComponentMap)


#
# schematic layout
#

class Component(models.Model):
    key = types.StringType()


class PlayerName(models.Model):
    first = types.StringType()
    last = types.StringType()
    full = types.StringType()


class PlayerId(models.Model):
    key_mlbam = types.StringType()
    key_retro = types.StringType()
    key_fangraphs = types.StringType()
    key_fangraphs_minors = types.StringType()
    key_bbref = types.StringType()
    key_bbref_minors = types.StringType()
    key_bbpro = types.StringType()
    key_davenport = types.StringType()
    key_cbs = types.StringType()
    key_espn = types.StringType()
    key_yahoo = types.StringType()
    key_nfbc = types.StringType()


class PlayerHands(models.Model):
    bats = types.StringType()
    throws = types.StringType()


class Player(models.Model):
    ids = types.compound.ModelType(PlayerId)
    team_name = types.StringType()
    name = types.compound.ModelType(PlayerName)
    age = types.StringType()
    league = types.StringType()
    roles = types.compound.ListType(types.StringType())
    hands = types.compound.ModelType(PlayerHands)


class ProjectionLine(models.Model):
    player = types.compound.ModelType(Player)
    # enforce that "components" exists,
    # but not its contents
    components = types.compound.DictType(types.StringType)


class ProjectionSchematic(models.Model):
    batting = types.compound.ModelType(ProjectionLine)
    pitching = types.compound.ModelType(ProjectionLine)
