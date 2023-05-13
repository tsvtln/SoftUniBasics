# Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# Всички останали са "unknown".

question = str(input())
if question == 'banana' or question == 'apple' or question == 'kiwi' or question == 'cherry' or\
    question == 'lemon' or question == 'grapes':
    print('fruit')
elif question == 'tomato' or question == 'cucumber' or question == 'pepper' or question == 'carrot':
    print('vegetable')
else:
    print('unknown')
