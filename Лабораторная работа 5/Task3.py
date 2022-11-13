from random import randint

def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    my_list = list()
    while len(set(my_list)) < 15:
        my_list.append(randint(-10, 10))
    return list(set(my_list))

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
