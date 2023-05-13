animal = str(input())

if animal == 'dog':
    print('mammal')
# crocodile, tortoise, snake -> reptile
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    print('reptile')
else:
    print('unknown')