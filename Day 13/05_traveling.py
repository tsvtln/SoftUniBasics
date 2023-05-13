destination = input()
minimal_budget = float(input())

is_going = False
has_money = True

while not is_going:
    spending = float(input())
    minimal_budget -= spending
    if minimal_budget > 0:
        has_money = True
    elif minimal_budget <= 0:
        has_money = False
    if not has_money:
        print(f'Going to {destination}!')
        destination = input()
        if destination == 'End':
            is_going = True
            break
        minimal_budget = float(input())
