import random
import string
from itertools import product, islice
from pprint import pprint as pp


length = 3
exclude_words = ['pid']


def is_consonant(letter):
    return letter not in 'aeiou'


def name_filter(name):
    # Filter any double letters
    if any(x[0] == x[1] for x in zip(name, name[1:])):
        return False
    # Filter any double consonants
    if any(is_consonant(x[0]) and is_consonant(x[1]) for x in zip(name, name[1:])):
        return False
    return True


names = filter(name_filter, (''.join(x) for x in product(string.ascii_lowercase,
    repeat=length)))


pp(random.sample(list(names), 10))
