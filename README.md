# Projection Schematics

Baseball projection spreadsheets come (Steamer, PECOTA, GURU, etc)
in all shapes and sizes. This app allows users translate
distribution-specific data (e.g., component names ("mPA", "DBL", "3B"),
roles, names) to a normalized, uniform schema.

## Installation

This package is not yet in PyPI, so for now install via Pip:

```shell
$ pip install -e git@github.com:mattdennewitz/baseball-projection-schematics.git#egg=baseball-projection-schematics
```

or clone the repo and install with:

```shell
$ pip install /path/to/this/repo/
```

## Schematics

Translation is accomplished by defining a map (here called a schematic)
between column names in a projection spreadsheet and a new, normalized schema.

Check out an example schematic here:
[PECOTA Schematic](https://github.com/mattdennewitz/projection-normalization/blob/develop/contrib/schematics/pecota-2015.json).

## Configuration

Before a schematic can be generated, the schematic needs to know
which components it's on the hook for mapping. These components
(and, implicitly, the order of their output when used in processing)
are then made available in the schematic.

Example:

```javascript
{
    "components": {
        "batting": [
            "g", "pa", "ab", "h", "1b", "2b", "3b", "hr",
            "bb", "ibb", "r", "rbi", "sb", "cs", "hbp",
            "obp", "slg", "so", "avg", "sh", "sf"
        ],

        "pitching": [
            "g", "gs", "ip", "w", "l", "qs",
            "sv", "hld", "so", "h", "bb", "ibb",
            "er", "era", "whip", "hra", "hbp",
            "k_9", "bb_9", "k_bb"
        ]
    }
}
```

(The example above is included in this repo as `config.json-example`.)

## Schema generation

Once you've defined fields, you can generate a translation schematic.
To do so, use `generate-schema`.

### Example usage

```shell
$ generate-schema -c /path/to/config.json /path/to/output
```

## Translating projections

After defining a translation schematic, it's time to put it to use.
To translate projections, use `process-projections`.

### Example usage

```shell
$ process-projections -c /path/to/config.json       \
                      -t batting                    \
                      -s /path/to/schematic.json    \
                      -i /path/to/projection.csv    \
                      /path/to/output.csv
```
