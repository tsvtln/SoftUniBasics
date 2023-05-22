turns_of_game = int(input())
score, numbers_0_10, numbers_10_19, numbers_20_29, numbers_30_39, numbers_40_50, numbers_invalid = 0, 0, 0, 0, 0, 0, 0

for dice in range(turns_of_game):
    roll = int(input())
    if roll < 0 or roll > 50:
        score = score / 2
        numbers_invalid += 1
    elif 0 <= roll <= 9:
        score += roll * 0.2
        numbers_0_10 += 1
    elif 10 <= roll <= 19:
        score += roll * 0.3
        numbers_10_19 += 1
    elif 20 <= roll <= 29:
        score += roll * 0.4
        numbers_20_29 += 1
    elif 30 <= roll <= 39:
        score += 50
        numbers_30_39 += 1
    elif 40 <= roll <= 50:
        score += 100
        numbers_40_50 += 1

# percentage calculations
avg_0_10 = (numbers_0_10 / turns_of_game) * 100
avg_10_19 = (numbers_10_19 / turns_of_game) * 100
avg_20_29 = (numbers_20_29 / turns_of_game) * 100
avg_30_39 = (numbers_30_39 / turns_of_game) * 100
avg_40_50 = (numbers_40_50 / turns_of_game) * 100
avg_fails = (numbers_invalid / turns_of_game) * 100

print(f'{score:.2f}\nFrom 0 to 9: {avg_0_10:.2f}%\nFrom 10 to 19: {avg_10_19:.2f}%\nFrom 20 to 29: {avg_20_29:.2f}%\n'
      f'From 30 to 39: {avg_30_39:.2f}%\nFrom 40 to 50: {avg_40_50:.2f}%\nInvalid numbers: {avg_fails:.2f}%')
