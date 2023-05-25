control = int(input())
combination, password = 0, ''

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    if (a * b) + (c * d) == control:
                        print(f"{a}{b}{c}{d}", end=' ')
                        combination += 1
                        if combination == 4:
                            password = f"{a}{b}{c}{d}"
if combination >= 4:
    print()
    print(f"Password: {password}")
else:
    print()
    print('No!')
