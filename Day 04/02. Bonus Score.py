score = int(input())
final_score = 0
bonus = 0

if score <= 100:
    bonus += 5
elif 100 < score < 1000:
    bonus = (score * 0.2) + bonus
elif score > 1000:
    bonus = (score * 0.1) + bonus

if score % 2 == 0:
    bonus += 1
elif score % 10 == 5:
    bonus += 2

final_score = bonus + score
print(bonus)
print(final_score)
