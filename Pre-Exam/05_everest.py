days = 1
meters_required = 5364

while True:
    night = input()
    if night == "END":
        if meters_required < 8848:
            print("Failed!")
            print(f"{meters_required}")
            break
        else:
            print(f"Goal reached for {days} days!")
            break

    if night == "Yes":
        days += 1

    meters = int(input())

    if days > 5:
        print("Failed!")
        print(f"{meters_required}")
        break

    meters_required += meters

    if meters_required >= 8848:
        print(f"Goal reached for {days} days!")
        break
