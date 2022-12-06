from ipaddress import ip_network
from socket import create_connection, gethostbyaddr, gethostbyname, gethostname
from rich.table import Table
from rich import print


def scan_ports(ip_address: str, ports: list[int]) -> list[int]:
    open_ports = []
    # Task 1a). Hint: attempting to connect to port that is not open will
    # raise an exception.
    return open_ports


def scan_subnet(subnet: str, ports: list[int]) -> dict[str, list[int]]:

    ip_addresses = (str(item) for item in ip_network(subnet, strict=False))
    report = {}

    # Task 1b). Use the function gethostbyaddr. Using this function with an
    # IP address that is not assigned to a host will raise an exception.
    return report


if __name__ == '__main__':
    # Task 1c)
    subnet = '127.0.0.0/24'
    # Task 1d)
    ports = [22]
    report = scan_subnet(subnet, ports)

    table = Table(title=f'Report for subnet {subnet}')
    table.add_column('Hostname', style='cyan')
    table.add_column('IP address', style='green')
    table.add_column('Open ports', style='magenta', justify='center')

    for host in report:
        table.add_row(
            f'{host}',
            f'{gethostbyname(host)}',
            '; '.join(
                str(port) for port in report[host]
            )
        )
    print('\n', table, '\n')
