days, hours_pd = int(input()), int(input())
payment_total, payment_day = 0, 0

for day in range(1, days + 1):
    for hour in range(1, hours_pd + 1):
        if day % 2 == 0 and hour % 2 != 0:
            payment_day += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            payment_day += 1.25
        else:
            payment_day += 1
    payment_total += payment_day
    print(f"Day: {day} - {payment_day:.2f} leva")
    payment_day = 0

print(f"Total: {payment_total:.2f} leva")
