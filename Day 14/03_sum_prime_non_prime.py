GO = True
is_prime = True
prime = 0
non_prime = 0

while GO:
    inp = input()
    if inp == 'stop':
        GO = False
        continue
    else:
        inp = int(inp)
    if inp < 0:
        print("Number is negative.")
        continue
    elif inp == 0:
        continue
    else:
        for i in range(2, inp):
            if inp % i == 0:
                is_prime = False
                break
    if is_prime:
        prime += inp
    else:
        non_prime += inp
        is_prime = True

print(f'Sum of all prime numbers is: {prime}\nSum of all non prime numbers is: {non_prime}')
