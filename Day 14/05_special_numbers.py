inp = int(input())
for i in range(1111, 10000):
    is_special = True
    num_to_string = str(i)
    for z in range(len(num_to_string)):
        converted = int(num_to_string[z])
        if converted == 0 or inp % converted != 0:
            is_special = False
            break

    if is_special:
        print(i, end=' ')
