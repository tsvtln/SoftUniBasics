pages_num = int(input())
page_read_ph = int(input())
days_req = int(input())

# Общо време за четене на книгата: 212 страници / 20 страници за час = 10 часа общо
# Необходимите часове на ден: 10 часа / 2 дни = 5 часа на ден

hours_per_pg = pages_num // page_read_ph
result = hours_per_pg // days_req

print(result)