number = float(input())
if number <= 10:
    print("slow")
elif number <= 50:
    print("average")
elif number <= 150:
    print("fast")
elif number <= 1000:
    print("ultra fast")
else:
    print("extremely fast")
