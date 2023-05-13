start_number = int(input())
end_number = int(input())
magic_number = int(input())
run = 0
FMN = False

for num1 in range(start_number, end_number + 1):
    if FMN:
        break
    for num2 in range(start_number, end_number + 1):
        run += 1
        temp_number = num1 + num2
        if temp_number == magic_number:
            print(f'Combination N:{run} ({num1} + {num2} = {magic_number})')
            FMN = True
            break
if not FMN:
    print(f'{run} combinations - neither equals {magic_number}')
