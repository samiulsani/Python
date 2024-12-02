def split(s):
    l_count = 0
    r_count = 0
    current = ""
    new_string = []

    for c in s:
        current += c
        if c == 'L':
            l_count += 1
        else:
            r_count += 1

        if l_count == r_count:
            new_string.append(current)
            current = ""
            l_count = 0
            r_count = 0

    print(len(new_string))
    for ns in new_string:
        print(ns)

s = input().strip()
split(s)
