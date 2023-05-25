start = int(input())
end = int(input())

for fn in range(start, end + 1):
    for sn in range(start, end + 1):
        for tn in range(start, end + 1):
            for ln in range(start, end + 1):
                if fn % 2 == 0 and ln % 2 != 0:
                    if fn > ln:
                        if (sn + tn) % 2 == 0:
                            print(f'{fn}{sn}{tn}{ln}', end=' ')
                elif fn % 2 != 0 and ln % 2 == 0:
                    if fn > ln:
                        if (sn + tn) % 2 == 0:
                            print(f'{fn}{sn}{tn}{ln}', end=' ')
