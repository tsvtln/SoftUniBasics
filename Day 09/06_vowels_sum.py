text = input()
final_score = 0

for i in range(len(text)):
    if text[i] == 'a':
        final_score += 1
    if text[i] == 'e':
        final_score += 2
    if text[i] == 'i':
        final_score += 3
    if text[i] == 'o':
        final_score += 4
    if text[i] == 'u':
        final_score += 5
print(final_score)
