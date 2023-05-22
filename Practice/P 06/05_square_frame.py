entry = int(input())
print(f"+ {'- ' * (entry - 2)}+")
for line in range(entry - 2):
    print(f"| {'- ' * (entry - 2)}|")
print(f"+ {'- ' * (entry - 2)}+")
