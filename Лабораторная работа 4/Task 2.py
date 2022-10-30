str_dict = {}

def get_count_char(str_):
    str_ = str_.lower()
    for i in str_:             # TODO посчитать количество каждой буквы в строке в аргументе str_
        if i.isalpha():
            if i in str_dict: str_dict[i] += 1
            else: str_dict[i] = 1
    return str_dict

def get_new_dict(str_dict):
    dict_sum = sum(str_dict.values())
    for i in str_dict:
        str_dict[i] = round(str_dict[i] * (100 / dict_sum))
    print(str_dict)
    return str_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
