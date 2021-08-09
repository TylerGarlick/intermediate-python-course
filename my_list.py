def main():
    r = [4, -2, 10, -18, 22]
    print(r[2:6])
    print(f'len list of {r[-1]}')
    t = r.copy()
    print(f'is t the same as r? {t is r}')
    c = r[:]
    print(f'is t the same as r? {t is c}')


main()
