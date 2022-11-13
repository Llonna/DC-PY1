# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
dict = [{'dec': i, 'bin': bin(i), 'hex': hex(i), 'oct': oct(i)} for i in range(15+1)]

pprint(dict)