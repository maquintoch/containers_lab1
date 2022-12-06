from requests import post
from brute_force import *


def form_login(url: str, user: str, password: str) -> bool:
    # Task 3. Implement
    pass


if __name__ == '__main__':

    # Task 3. Provide a valid URL
    url = 'http://target2/'

    # Task 3. Load usernames and passwords using the functions you implemented.
    users = load_users()
    passwords = load_passwords()

    def login(user, password): return form_login(url, user, password)

    report(brute_force(login, users, passwords), url)
