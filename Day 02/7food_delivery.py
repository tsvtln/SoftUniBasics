chicken = 10.35
fish = 12.40
vegan = 8.15
delivery = 2.50

num_chicken = int(input())
num_fish = int(input())
num_vegan = int(input())

desert = ((num_chicken * chicken) + (num_fish * fish) + (num_vegan * vegan)) * 0.2
final_price = ((num_chicken * chicken) + (num_fish * fish) + (num_vegan * vegan)) + desert + delivery

print(final_price)