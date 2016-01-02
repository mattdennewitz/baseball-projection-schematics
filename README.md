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
[PECOTA Schematic](https://github.com/mattdennewitz/projection-normalization/blob/develop/contrib/schematics/season-2015/pecota.json).

## Configuration

Before a schematic can be created, the app needs to know
which components it's on the hook for mapping.

Create a JSON file called `config.json` with the following structure:

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

Schemas map fields with expectedly varying names to canonical representations,
e.g., mapping "AGE" from one system and "playerAge" from another to
simply "age" in your output.

Use `bb-generate-schema` to generate a empty schematics, and then
map field names from CSV headers to the fields in the schematic.

### Example usage

```shell
$ bb-generate-schema -c /path/to/config.json /path/to/output
```

## Translating projections

After defining a translation schematic, it's time to put it to use.
To translate projections, use `bb-process-projections`.

```shell
$ bb-process-projections        \
    -c /path/to/config.json     \
    -t batting                  \
    -s /path/to/schematic.json  \
    -i /path/to/projection.csv  \
    /path/to/output.csv
```

This will output the normalized projection in CSV format.
