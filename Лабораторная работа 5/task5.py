def get_random_password() -> str:
    ...  # TODO написать функцию генерации случайных паролей



import random


def get_random_password(n=8):
    symbols_str = "ASDFGHJKLZXCVBNMQWERTYUIOPasdfghjklpqowieurytzxcvbnm0123456789"
    return random.sample(symbols_str, n)


print(get_random_password())