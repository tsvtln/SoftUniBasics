man = int(input())
woman = int(input())
tables = int(input())
seats = tables * 2
TABLES = False

while not seats <= 0:
    for meets_man in range(1, man + 1):
        for meets_woman in range(1, woman + 1):
            print(f'({meets_man} <-> {meets_woman})', end=' ')
            seats -= 2
            if seats <= 0:
                TABLES = True
            if TABLES:
                break
        if TABLES:
            break
        if meets_man == man:
            seats = 0
