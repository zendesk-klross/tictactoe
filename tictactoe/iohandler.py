import click
import os
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
    def pretty_print_grid(grid):
        for row in grid:
            colored_row = [' | '.join([click.style(cell, fg='red') if cell == 'X' else click.style(cell, fg='green') if cell == 'O' else click.style(cell, fg='bright_black') if cell.isdigit() else cell for cell in row])]
            click.echo('-' * (len(row) * 4 + 1))
            click.echo('| ' + colored_row[0] + ' |')
            click.echo('-' * (len(row) * 4 + 1))
