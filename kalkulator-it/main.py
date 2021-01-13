import click

@click.command()
@click.option('-t','--target','target',type=str,required=True,
              help='Destination number (dec,bin,oct,hex)')
@click.argument('number',type=int)
def calculate(target, number):
    """
    Simple program that converts decimal computer number.
    """
    converter = ['bin','hex','oct']
    if target in converter:
        if target == 'bin':
            click.echo(f'Result : {bin(number)[2:]} \n')
        elif target == 'oct':
            click.echo(f'Result : {oct(number)[2:]} \n')
        elif target == 'hex':
            click.echo(f'Result : {hex(number)[2:]} \n')
    else:
        click.echo('Arguments error')