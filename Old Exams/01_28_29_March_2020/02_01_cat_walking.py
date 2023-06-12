def cat_walk(duration_walk: int, times_talk: int, calories: int):
    total_time = times_talk * duration_walk
    calories_burned = total_time * 5
    if calories_burned >= calories / 2:
        return True, calories_burned
    else:
        return False, calories_burned


walk_dur, walk_time, intake_calories = int(input()), int(input()), int(input())
result = cat_walk(walk_dur, walk_time, intake_calories)
if result[0]:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {result[1]}.')
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {result[1]}.")
