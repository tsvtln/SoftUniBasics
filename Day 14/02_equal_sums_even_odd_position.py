num1 = int(input())
num2 = int(input())

for num in range(num1, num2 + 1):
    even = 0
    odd = 0
    num = str(num)
    for i in range(len(num)):
        if i % 2 == 0:
            even += int(num[i])
        else:
            odd += int(num[i])
    if even == odd:
        print(num, end=' ')

