from mylib.bot import scrape
import click

@click.command()
@click.option('--name',
              help='Web page we want to scrape')

def cli(name):
    res = scrape(name)
    click.echo(click.style(f"{res}", fg="blue"))
        #click.echo(click.style(f"{res}", fg="blue", bg="white"))

if __name__ == '__main__':
    cli()
