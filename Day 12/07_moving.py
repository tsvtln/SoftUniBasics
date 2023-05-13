free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

total_space = free_space_height * free_space_length * free_space_width

is_done = False

while not is_done:
    boxes = input()
    if boxes == 'Done':
        is_done = True
    else:
        boxes = int(boxes)
        total_space -= boxes
    if total_space < 0:
        is_done = True

if total_space > 0:
    print(f'{total_space} Cubic meters left.')
elif total_space < 0:
    print(f'No more free space! You need {abs(total_space)} Cubic meters more.')
