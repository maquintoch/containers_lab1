from itertools import product
from typing import Callable, Iterable
from rich.table import Table
from rich import print

LogInFunction = Callable[[str, str], bool]
Pairs = Iterable[tuple[str, str]]


# Task 2a)


def brute_force(
    login: LogInFunction,
    users: list[str],
    passwords: list[str]
) -> Pairs:
    # Task 2b)
    pass
    pairs = product(users, passwords)
    return filter(lambda pair: login(*pair), pairs)


def report(pairs: Pairs, name: str) -> None:

    table = Table(title=f'Report for {name}')
    table.add_column('User name', style='cyan')
    table.add_column('Password', style='green')

    for host, password in pairs:
        table.add_row(f'{host}', f'{password}')
    print('\n', table, '\n')
