def main():
    r = range(5)
    print(r)
    print(type(r))
    for item in r:
        print(item)
    l = list(range(2))
    print(l)
    print(type(l))
    for item in l:
        print(item)

    for i, v in enumerate([6, 345, 67, 1, 99, 234]):
        print(f'Index{i}, value {v}')


main()
