from random import sample
import string

def get_random_password(n = 8) -> str:
    ...  # TODO написать функцию генерации случайных паролей
    if not isinstance(n, int): raise TypeError("n must be integer")
    if n <= 0: raise ValueError("n must be greater than 0")

    password = (sample(string.digits + string.ascii_lowercase + string.ascii_uppercase, n))
    return ("".join(password))

print(get_random_password())