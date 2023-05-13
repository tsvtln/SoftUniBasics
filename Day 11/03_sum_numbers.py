num = int(input())
dynamic = 0

while True:
    n = int(input())
    dynamic += n
    if dynamic >= num:
        print(f'{dynamic}')
        break
