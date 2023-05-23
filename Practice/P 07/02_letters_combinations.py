start = input()
finish = input()
skip = input()
combos = 0

for fl in range(ord(start), ord(finish) + 1):
    for sl in range(ord(start), ord(finish) + 1):
        for tl in range(ord(start), ord(finish) + 1):
            if ord(skip) != tl and ord(skip) != sl and ord(skip) != fl:
                print(f"{chr(fl)}{chr(sl)}{chr(tl)}", end=' ')
                combos += 1

print(combos)
