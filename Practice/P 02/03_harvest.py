from math import ceil, floor
x = int(input())  # golemina loze
y = float(input())  # grozde za kv m
z = int(input())  # nujni litri
c = int(input())  # broi rabotnici

trzv = x * 0.4  # total rekolta za vino
kg_grozde = trzv * y
litra_vino = kg_grozde / 2.5

if litra_vino >= z:
    print(f'Good harvest this year! Total wine: {floor(litra_vino)} liters.')
    left_vino = litra_vino - z
    per_worker = left_vino / c
    print(f'{ceil(left_vino)} liters left -> {ceil(per_worker)} liters per person.')

else:
    needed_wine = z - litra_vino
    print(f'It will be a tough winter! More {floor(needed_wine)} liters wine needed.')
