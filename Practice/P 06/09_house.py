""" DOESN'T WORK"""

from math import ceil
entry = int(input())
stars = 0
drip_edge = ceil((entry / 2) - 1) * "-"
rows = ceil((entry + 1) / 2)

for roof in range(rows):
    if roof == 0:
        if entry % 2 == 0:
            print(f"{drip_edge}{2 * '*'}{drip_edge}")
            stars = 2
        else:
            print(f"{drip_edge}*{drip_edge}")
            stars = 1

    elif roof != 0:
        stars += 2
        drip_edge = ceil((entry - (stars + 1)) / 2) * "-"
        print(f"{drip_edge}{stars * '*'}{drip_edge}")

# Build the body
    house_body = entry - (int((entry + 1) / 2))
    for body in range(1, house_body + 1):
        print(f"|{(entry - 2) * '*'}|")

#     for roof in range(1, rows + 1):
#         if stars != entry:
#             print(f"{'_' * roof}{'*' * stars}{'_' * roof}")
#         else:
#             print(f"{'*' * stars}")
#         stars += 2
# elif entry % 2 != 0:
#     stars = 1

""" WORKING CODE """
"""
from math import ceil
number = int(input())
n_count = 0
dashes = ceil((number / 2) - 1) * "-"
for n in range(ceil(number / 2)):
    if n == 0:
        if number % 2 == 0:
            print(f"{dashes}{2 * '*'}{dashes}")
            n_count = 2
        else:
            print(f"{dashes}*{dashes}")
            n_count = 1
    elif n != 0:
        n_count += 2
        dashes_2 = ceil((number - (n_count + 1))/2) * "-"
        print(f"{dashes_2}{n_count * '*'}{dashes_2}")
for n in range(1, number - (int((number + 1)/2)) + 1):
    print(f"|{(number - 2) * '*'}|")
    """
