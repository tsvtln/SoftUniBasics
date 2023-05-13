from math import floor
# scores
W = 2000
F = 1200
SF = 720
total_score = 0
wins = 0

# inputs
number_of_tournaments = int(input())
season_start_score = int(input())
total_score += season_start_score

for _ in range(number_of_tournaments):
    tournament_result = input()
    if tournament_result == 'W':
        wins += 1
        total_score += W
    elif tournament_result == 'F':
        total_score += F
    elif tournament_result == 'SF':
        total_score += SF

# final points = total_score
avg_pts = (total_score - season_start_score) / number_of_tournaments
prc_wins = (wins / number_of_tournaments) * 100
print(f'Final points: {total_score}\nAverage points: {floor(avg_pts)}\n{prc_wins:.2f}%')
