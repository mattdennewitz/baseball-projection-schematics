from __future__ import unicode_literals
import json

import schematics

from .exceptions import ConfigError
from .models import ConfigSchematic


__all__ = ('read_config', )


def read_from_file(config_fp):
    try:
        # load and validate config
        return ConfigSchematic(json.load(config_fp))
    except (schematics.exceptions.ModelValidationError,
            schematics.exceptions.ModelConversionError) as exc:
        raise ConfigError('Could not load configuration: %s' % exc)
