import random
from typing import Optional


def reverse_list(input_list: list) -> list:
    if type(input_list) == list:
        return [item for item in reversed(input_list)]
        # return input_list.reverse()
    else:
        raise TypeError


def delete_repeats(input):
    no_doubles = []
    for item in input:
        if item not in no_doubles:
            no_doubles.append(item)
    return no_doubles


def count_nonunique(input):
    uniques = {}
    for item in input:
        if item not in uniques:
            uniques[item] = 1
        else:
            uniques[item] += 1
    result = 0
    for item in uniques:
        if uniques[item] > 1:
            result += 1
    return result


def get_digits(number: int) -> list:
    digits = []
    if type(number) == int and number > 0:
        while number > 0:
            digits.append(number % 10)
            number = number // 10
        return [item for item in reversed(digits)]

    else:
        raise TypeError


def count_even_odd(number: int):
    d = {'even': 0, 'odd': 0}
    if type(number) == int and number > 0:
        while number > 0:
            if (number % 10) % 2 == 0:
                d['even'] += 1
            else:
                d['odd'] += 1
            number = number // 10
        return d
    else:
        raise TypeError


def diff_objects(object1, object2):
    return [item for item in object1 if item not in object2]


def check_coords(*args) -> list:
    validated_coords = []
    for lat, lng in args:
        item = {'lat': lat,
                'lng': lng,
                'error': ''}
        if item['lat'] > 90 or item['lat'] < -90:
            item['error'] += f'Неверно задана широта: {item["lat"]} (должна быть от -90.0 до 90.0).'
        if item['lng'] > 180 or item['lng'] < -180:
            item[
                'error'] += f'Неверно задана долгота: {item["lng"]} (должна быть от -180.0 до 180.0)'
        if len(item['error']) > 0:
            validated_coords.append(item)
    return validated_coords


# from _collections import defaultdict

def count_words(string: str) -> dict:
    if len(string) == 0:
        raise TypeError
    else:
        list_of_words = string.lower().split(' ')
        dict_of_words = {}
        for word in list_of_words:
            if word not in dict_of_words:
                dict_of_words[word] = 1
            else:
                dict_of_words[word] += 1
        return dict_of_words


def check_brackets(string: str):
    brackets = []
    brackets_map = {')': '(', '}': '{', ']': '['}
    for index, item in enumerate(string):
        if item in ('(', '[', '{'):
            brackets.append(item)
        if item in (')', ']', '}'):
            if len(brackets) == 0:
                return index + 1
            else:
                if brackets_map[item] != brackets.pop():
                    return index + 1

    if len(brackets) > 0:
        return len(brackets)
    return -1


from random import choice

from string import digits, ascii_lowercase, ascii_uppercase, punctuation


def generate_password(strength: int = 1, length: Optional[int] = None,
                      from_source: Optional[str] = None):
    patterns = {'0': digits, '1': digits + ascii_lowercase,
                '2': digits + ascii_lowercase + ascii_uppercase,
                '3': digits + ascii_lowercase + ascii_uppercase + punctuation}
    if length is None:
        length = random.randint(4, 16)

    if from_source is not None:
        password = ''.join([random.choice(list(from_source)) for x in range(length)])
        return password
    else:
        if strength > 3:
            strength = '3'
        else:
            strength = str(strength)

        password = ''.join(
                [random.choice(list(patterns[strength])) for x in range(length)])
        return password



if __name__ == '__main__':
# reverse_list(['abc', 'def'])
# reverse_list(11)
# print(delete_repeats(['abc', 'abc', 'def', 'abc']))
# print(delete_repeats('qwerrty'))

# print(count_nonunique('qwweerrty'))
# print(get_digits(1234))
# print(even_noteven(1111))
# print(diff_objects('1111', '2122'))
# print(check_coords(
# (0.0, 1.0),
# (-35.7, -100.7),
# (-95.0, 120.5),
# (88.8, 190.5),
# (17.33, 18.46),
# (-120.0, -200.1)))
# print(count_words('qqq www eee qqq qqq WWW'))
# print(check_brackets('((()))))'))
    print(generate_password(strength=9, length=10))
