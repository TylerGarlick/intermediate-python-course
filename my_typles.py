#!/usr/bin/env python3

def minmax(items):
    """
    Returns the maximum and minimum of the the collection
    :param items:
    :return: min and max
    """
    return min(items), max(items)


def main():
    a = ((1, 2), (10, 20), (10, 200))

    for l1 in a:
        print(l1)
        for l2 in l1:
            print(l2)

    print(a)


if __name__ == '__main__':
    items = (3, 88, 11, 22, 90)
    lower, upper = minmax(items)
    print(f'Min: {lower} Max: {upper}')
    if 3 in items:
        print('I have a 3')
    if 99 not in items:
        print('I do not have 99')
