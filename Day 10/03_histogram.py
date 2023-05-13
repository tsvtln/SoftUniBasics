num = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for _ in range(num):
    get_num = int(input())
    if get_num < 200:
        p1 += 1
    elif get_num <= 399:
        p2 += 1
    elif get_num <= 599:
        p3 += 1
    elif get_num <= 799:
        p4 += 1
    elif get_num >= 800:
        p5 += 1

prc_1 = p1 / num * 100
prc_2 = p2 / num * 100
prc_3 = p3 / num * 100
prc_4 = p4 / num * 100
prc_5 = p5 / num * 100

print(f'{prc_1:.2f}%')
print(f'{prc_2:.2f}%')
print(f'{prc_3:.2f}%')
print(f'{prc_4:.2f}%')
print(f'{prc_5:.2f}%')
