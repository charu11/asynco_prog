def find_divisibles(inrange, div_by):
    print('finding the nums in range {} divisible by {}'.format(inrange, div_by))
    located = []

    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
    print('Done w/ nums in range {} divisible by {} '.format(inrange, div_by))
    return located


def main():
    divis1 = find_divisibles(508000, 34113)
    divis2 = find_divisibles(100052, 3210)
    divis3 = find_divisibles(500, 3)


if __name__ == '__main__':
    main()

