import unicodecsv as csv

import click


@click.command()
@click.argument('input_fp', type=click.File('rb'), required=True)
@click.argument('output_fp', type=click.File('w'), required=True)
def csvert(input_fp, output_fp):
    reader = csv.reader(input_fp)
    widths = [-1, -1]

    rows = list(reader)
    headers = rows.pop(0)

    for row in rows:
        for i, key in enumerate(headers):
            key_len = len(key)
            value_len = len(row[i])

            if key_len > widths[0]:
                widths[0] = key_len

            if value_len > widths[1]:
                widths[1] = value_len

    sep = '+-' + '-+-'.join('-' * w for w in widths) + '-+'

    output_fp.write(sep + '\n')

    for i, row in enumerate(rows):
        output = []

        for h, key in enumerate(headers):
            value = row[h]
            output.append((
                key.ljust(widths[0]),
                value.ljust(widths[1])
            ))

        for step in output:
            output_fp.write( '| %s |\n' % ( ' | '.join(step) ) )

        output_fp.write(sep + '\n')


if __name__ == '__main__':
    csvert()
