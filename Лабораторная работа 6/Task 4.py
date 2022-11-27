import json

INPUT_FILE = "input_1.csv"


def csv_to_list_dict(filename, delimiter = ',', new_line = '\n') -> list[dict]:
    # TODO реализовать конвертер из csv в json
    _dict = {}
    headers = []
    list_lines = []
    with open(filename) as file:
        headers = (file.readline().split(delimiter))
        headers[-1] = headers[-1][:-1]
        for line in file:
            list_lines.append((line.split(delimiter)))
            list_lines[-1] = list_lines[-1][:-1]

    for line in list_lines:
        for i, key, value in zip(range(len(headers)-1), headers, line):
            if key not in _dict:
                _dict[key] = []
            _dict[key].append(value)
    return _dict



print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))