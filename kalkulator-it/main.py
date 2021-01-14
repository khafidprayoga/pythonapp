import sys
import click
from dec import decimal
from bin import binary
from oct import octal
from hex import hexdec

@click.command()
@click.version_option()
@click.option('-s','--src','source',type=str,required=True,
              help='Source number (dec,bin,oct,hex)')
@click.option('-d','--dst','destination',type=str,required=True,
              help='Destination number (dec,bin,oct,hex)')
@click.argument('number',type=str)
def calculate(source, destination, number):
    """
    Simple program that converts computer number.
    """
    try:
        if source == 'bin':
            if destination == 'dec':
                click.echo(f'Result\t: {binary.to_dec(number)}')
            elif destination == 'oct':
                click.echo(f'Result\t: {binary.to_oct(number)}')
            elif destination == 'hex':
                click.echo(f'Result\t: {binary.to_hex(number)}')
            else:
                click.echo('Destination error, not a valid value.')
                sys.exit(2)

        elif source == 'dec':
            number = int(number)
            if destination == 'bin':
                click.echo(f'Result\t: {decimal.to_bin(number)}')
            elif destination == 'oct':
                click.echo(f'Result\t: {decimal.to_oct(number)}')
            elif destination == 'hex':
                click.echo(f'Result\t: {decimal.to_hex(number)}')
            else:
                click.echo('Destination error, not a valid value.')
                sys.exit(2)

        elif source == 'oct':
            if destination == 'bin':
                click.echo(f'Result\t: {octal.to_bin(number)}')
            elif destination == 'dec':
                click.echo(f'Result\t: {octal.to_dec(number)}')
            elif destination == 'hex':
                click.echo(f'Result\t: {octal.to_hex(number)}')
            else:
                click.echo('Destination error, not a valid value.')
                sys.exit(2)

        elif source == 'hex':
            if destination == 'bin':
                click.echo(f'Result\t: {hexdec.to_bin(number)}')
            elif destination == 'dec':
                click.echo(f'Result\t: {hexdec.to_dec(number)}')
            elif destination == 'oct':
                click.echo(f'Result\t: {hexdec.to_oct(number)}')
            else:
                click.echo('Destination error, not a valid value.')
                sys.exit(2)
        else:
            click.echo('Source error, not a valid value.')
            sys.exit(1)
    except ValueError as err:
        click.echo('Error: %s ' % err)
