numbers = []

with open('in.txt') as fi:
    lines = fi.readlines()
    for l in lines:
        words = l.split(' ')
        for w in words:
            try:
                n = int(w)
                if n != 2019 and n not in numbers:
                    numbers.append(n)
            except ValueError:
                continue

with open('out.csv', 'w+') as fo:
    lines = list(map(lambda x: f'"{x}",\r\n', numbers))
    lines.insert(0, '"Num",\r\n')
    fo.writelines(lines)