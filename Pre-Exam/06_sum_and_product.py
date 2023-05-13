num = int(input())
is_n_5 = False
is_spl_3 = False
number_found = False

if num % 3 == 0:
    is_spl_3 = True

if num % 10 == 5:
    is_n_5 = True

for a in range(1, 10):
    for b in range(9, a, -1):
        for c in range(0, 10):
            for d in range(9, c, -1):
                if number_found:
                    break
                summ_iterations = a + b + c + d
                multi_iterations = a * b * c * d

                if summ_iterations == multi_iterations and is_n_5:
                    print(f"{a}{b}{c}{d}")
                    number_found = True
                    break
                elif multi_iterations // summ_iterations == 3 and is_spl_3:
                    print(f"{d}{c}{b}{a}")
                    number_found = True
                    break
        if number_found:
            break
    if number_found:
        break
if not number_found:
    print(f'Nothing found')
