goal = 10000
igh = 'Going home'  # is going home
ttls = 0  # total steps

while ttls < goal:
    steps = input()
    if steps != igh:
        steps = int(steps)
        ttls += steps
    elif steps == igh:
        steps = int(input())
        ttls += steps
        break

df = abs(ttls - goal)

if ttls > goal:
    print(f'Goal reached! Good job!\n{df} steps over the goal!')
elif ttls < goal:
    print(f'{df} more steps to reach goal.')
