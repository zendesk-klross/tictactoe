import click
import os
import time
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


class IOHandler:

    @staticmethod
    def input(prompt):
        return click.prompt(prompt)

    @staticmethod
    def output(message):
        click.echo(message)

    @staticmethod
    def input_options(message, options):
        completer = WordCompleter(options, ignore_case=True)
        choice = prompt(message, completer=completer)
        return choice

    @staticmethod
    def output_from_file(file_path):
        absolute_path = os.path.abspath(file_path)

        with open(absolute_path, 'r') as file:
            content = file.read()
        click.echo(content)

    @staticmethod
    def clear_screen():
        click.clear()

    @staticmethod
    def pretty_print_grid(grid, token1, token2):
        cell_width = 4
        for row in grid:
            colored_row = [' | '.join([click.style(cell.ljust(cell_width), fg='magenta') if cell == token1
                                       else click.style(cell.ljust(cell_width), fg='cyan') if cell == token2
            else click.style(cell.ljust(cell_width), fg='bright_black') if cell.isdigit()
            else cell.ljust(cell_width) for cell in row])]
            click.echo('-' * (len(row) * (cell_width + 3) + 1))
            click.echo('| ' + colored_row[0] + ' |')
            click.echo('-' * (len(row) * (cell_width + 3) + 1))

    @staticmethod
    def progress_bar(message):
        with click.progressbar(range(70), label=message) as bar:
            for item in bar:
                time.sleep(0.02)