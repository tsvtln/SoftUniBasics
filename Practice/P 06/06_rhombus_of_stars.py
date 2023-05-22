entry = int(input())
# top side
for top in range(1, entry + 1):
    print(f"{' ' * (entry - top)}{'* ' * top}")

# bottom side
for bot in range(entry - 1, 0, -1):
    print(f"{' ' * (entry - bot)}{'* ' * bot}")


