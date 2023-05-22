months = int(input())
water_bill = 20
internet_bill = 15
other_bill = 0

total_electricity = 0
total_water = 0
total_internet = 0
total_other = 0
total_all = 0

for month in range(months):
    electricity_bill = float(input())
    total_electricity += electricity_bill
    total_internet += internet_bill
    total_water += water_bill
    other_bill = (electricity_bill + water_bill + internet_bill) + ((electricity_bill +
                                                                     water_bill + internet_bill) * 0.2)
    total_other += other_bill
    total_all += electricity_bill + internet_bill + water_bill + other_bill

avg_expenses = total_all / months
print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {avg_expenses:.2f} lv")
