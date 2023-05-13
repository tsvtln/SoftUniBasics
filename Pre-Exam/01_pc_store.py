price_in_dollars_processor = float(input())
price_in_dollars_video_card = float(input())
price_in_dollars_ram = float(input())
number_of_rams = int(input())
discount = float(input())

dollar_value = 1.57

procesor_in_leva = price_in_dollars_processor * dollar_value
video_card_in_leva = price_in_dollars_video_card * dollar_value
ram_in_leva = (price_in_dollars_ram * dollar_value) * number_of_rams

discounted_processor = procesor_in_leva - (procesor_in_leva * discount)
discounted_video_card = video_card_in_leva - (video_card_in_leva * discount)
# discounted_ram = ram_in_leva - (ram_in_leva * discount)

total_sum = discounted_processor + discounted_video_card + ram_in_leva

print(f"Money needed - {total_sum:.2f} leva.")
