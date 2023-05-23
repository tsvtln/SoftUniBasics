number = int(input())

for fn in range(1, 10):
    for sn in range(1, 10):
        for tn in range(1, 10):
            for ln in range(1, 10):
                if fn + sn == tn + ln:
                    if number % (fn + sn) == 0:
                        print(f'{fn}{sn}{tn}{ln}', end=' ')

"""TESTS"""
# print(numbers_lucky)
# numbers_lucky = []
# for lucky in range(1, number + 1):
#     for lucky2 in range(1, number + 1):
#         if number % (lucky2 + lucky) == 0:
#             numbers_lucky.append(lucky2)
