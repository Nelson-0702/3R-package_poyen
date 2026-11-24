"""CLI script for the 3R-package_poyen package. This will be called on the command line"""

import click

from 3R-package_poyen.3R-package_poyen import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def 3R-package_poyen_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
