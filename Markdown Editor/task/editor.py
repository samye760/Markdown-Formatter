import sys
from typing import List


def helper() -> None:
    print("Available formatters: plain bold italic header link inline-code new-line")
    print("Special commands: !help !done")


def done() -> None:
    with open('output.md', 'w') as output:
        output.writelines(total)
    sys.exit()


def plain() -> str:
    return input("Text: ")


def bold() -> str:
    return ''.join(['**', input("Text: "), '**'])


def italic() -> str:
    return ''.join(['*', input("Text: "), '*'])


def inline_code() -> str:
    return ''.join(['`', input("Text: "), '`'])


def link() -> str:
    return ''.join(['[', input("Label: "), ']', '(', input("URL: "), ')'])


def header() -> str:

    while True:

        level: int = int(input("Level: "))

        if not 1 <= level <= 6:
            print("The level should be within the range of 1 to 6")
            continue

        return f"{level * '#'} {input('Text: ')}\n"


def new_line() -> str:
    return '\n'


def lists() -> str:

    while True:

        try:
            num_rows: int = int(input("Number of rows: "))
        except ValueError:
            print("Number of rows must be an integer")
            continue

        if num_rows < 1:
            print("Number of rows should be greater than zero")
            continue

        break

    ret_list: str = ''

    if formatter == 'ordered-list':
        for idx in range(1, num_rows + 1):
            ret_list += f'{idx}. {input(f"Row #{idx}: ")}\n'

    else:
        for idx in range(1, num_rows + 1):
            ret_list += f'* {input(f"Row #{idx}: ")}\n'

    return ret_list


total: List[str] = []

while True:

    formatter: str = input("Choose a formatter: ")

    if formatter not in ('!help', '!done', 'plain', 'bold', 'italic', 'header', 'link',
                         'inline-code', 'new-line', 'ordered-list', 'unordered-list'):
        print('Unknown formatting type or command')
        continue

    if formatter == '!help':
        helper()
        continue
    elif formatter == '!done':
        done()
    elif formatter == 'plain':
        total.append(plain())
    elif formatter == 'bold':
        total.append(bold())
    elif formatter == 'italic':
        total.append(italic())
    elif formatter == 'header':
        total.append(header())
    elif formatter == 'link':
        total.append(link())
    elif formatter == 'inline-code':
        total.append(inline_code())
    elif formatter == 'new-line':
        total.append(new_line())
    elif formatter in ('ordered-list', 'unordered-list'):
        total.append(lists())

    print(*total, sep='')
