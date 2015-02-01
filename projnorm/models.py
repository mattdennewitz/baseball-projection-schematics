from schematics import models, types


class ComponentMap(models.Model):
    batting = types.compound.ListType(types.StringType())
    pitching = types.compound.ListType(types.StringType())


class ConfigSchematic(models.Model):
    "Schematic for schema generation configuration"

    components = types.compound.ModelType(ComponentMap)
