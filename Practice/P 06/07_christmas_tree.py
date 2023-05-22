entry = int(input())
# left side
for left in range(entry + 1):
    print(f"{' ' * (entry - left)}{'*' * left} | ", end='')
    print(f"{'*' * left}")
