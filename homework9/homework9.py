import re


def split_email(email):
    email_pattern = r'^(?P<username>[a-zA-Z0-9][a-zA-Z0-9._%+-]*[a-zA-Z0-9])@(?P<domain>[a-zA-Z0-9-]+\.[a-zA-Z]{2,})$'

    match = re.match(email_pattern, email)
    if match:
        username = match.group('username')
        domain = match.group('domain')
        print(f"username: {username}")
        print(f"domain: {domain}")
    else:
        print("Некорректный email адрес.")


def main():
    email = input("Введите email: ")

    split_email(email)


main()
