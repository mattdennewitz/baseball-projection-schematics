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

## Finding projections

You may find the projections here:

- Steamer - scraped from [Fangraphs](http://www.fangraphs.com/projections.aspx?pos=all&stats=pit&type=steamer&team=0&lg=all&players=0&sort=20%2cd)
    using [this importer](https://github.com/mattdennewitz/mlb-fangraphs-steamer-importer).
    (:free:)
- [Guru](http://baseballguru.com/bbinside4.html) (:free:)
- ZiPS - coming soon (:free:)
- CAIRO - coming soon (:free:)
- PECOTA - coming soon (:moneybag:)
- Davenport - coming soon (:free:)

## Schematics

Translation is accomplished by defining a map (here called a schematic)
between column names in a projection spreadsheet and a new, normalized schema.

Check out an example schematic here:
[PECOTA Schematic](https://github.com/mattdennewitz/projection-normalization/blob/develop/contrib/schematics/season-2015/pecota.json).

## Schema generation

Schemas map fields with expectedly varying names to canonical representations,
e.g., mapping "AGE" from one system and "playerAge" from another to
simply "age" in your output.

Use `bb-generate-schema` to generate a empty schematics, and then
map field names from CSV headers to the fields in the schematic.

### Example usage

```shell
$ bb-generate-schema /path/to/output
```

## Translating projections

After defining a translation schematic, it's time to put it to use.
To translate projections, use `bb-process-projections`.

```shell
$ bb-process-projections        \
    -t batting                  \
    -s /path/to/schematic.json  \
    -i /path/to/projection.csv  \
    /path/to/output.csv
```

This will output the normalized projection in CSV format.
