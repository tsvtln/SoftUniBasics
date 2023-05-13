length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

size = length * width * height
size_in_liters = size * 0.001
space_taken = size_in_liters * (1 - percent)

print(space_taken)
