nylon = 1.50
paint = 14.50
paint_buster = 5.00
bag = 0.40

num_nylon = int(input()) + 2
num_paint = int(input())
num_paint_buster = int(input())
num_workers = int(input())

# Сума за найлон: (10 + 2) * 1.50 = 18 лв.
# Сума за боя: (11 + 10%) * 14.50 = 175.45 лв.
# Сума за разредител: 4 * 5.00 = 20.00 лв.
# Сума за торбички: 0.40 лв.
# Обща сума за материали: 18 + 175.45 + 20.00 + 0.40 = 213.85 лв.
# Сума за майстори: (213.85 * 30%) * 8 = 513.24 лв.
# Крайна сума: 213.85 + 513.24 = 727.09 лв.

nylon_sum = num_nylon * nylon
paint_sum = (num_paint + (num_paint * 0.10)) * paint
paint_buster_sum = num_paint_buster * paint_buster
materials_sum = nylon_sum + paint_sum + paint_buster_sum + bag
workers_sum = (materials_sum * 0.3) * num_workers
final_sum = materials_sum + workers_sum

print(final_sum)
