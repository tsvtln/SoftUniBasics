n = int(input())
l = int(input())

for a in range(1, n):
    for b in range(1, n):
        for c in range(ord("a"), ord("a") + l):
            for d in range(ord("a"), ord("a") + l):
                for e in range(max(a, b) + 1, n + 1):
                    print(f"{a}{b}{chr(c)}{chr(d)}{e}", end=" ")
