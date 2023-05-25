start, end, magic_number = int(input()), int(input()), int(input())

combinations, first_number, second_number = 0, '', ''
FOUND = False

for first_number in range(start, end + 1):
    for second_number in range(start, end + 1):
        test_magic = first_number + second_number
        combinations += 1
        if test_magic == magic_number:
            FOUND = True
            first_number = first_number
            second_number = second_number
            break
    if FOUND:
        break

if FOUND:
    print(f"Combination N:{combinations} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combinations} combinations - neither equals {magic_number}")
