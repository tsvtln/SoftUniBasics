microbus = 200
truck = 175
train = 120

used_microbus = 0
used_truck = 0
used_train = 0
total_weight = 0
total_price = 0

number_of_shipments = int(input())
for runs in range(number_of_shipments):
    shipment_weight = int(input())
    total_weight += shipment_weight
    if shipment_weight <= 3:
        used_microbus += shipment_weight
        total_price += microbus * shipment_weight
    elif 4 <= shipment_weight <= 11:
        used_truck += shipment_weight
        total_price += truck * shipment_weight
    else:
        used_train += shipment_weight
        total_price += train * shipment_weight

average_price_per_shipment = total_price / total_weight
percent_microbus = used_microbus / total_weight * 100
percent_truck = used_truck / total_weight * 100
percent_train = used_train / total_weight * 100

print(f'{average_price_per_shipment:.2f}\n{percent_microbus:.2f}%\n{percent_truck:.2f}%\n{percent_train:.2f}%')
