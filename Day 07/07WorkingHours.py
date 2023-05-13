hour = int(input())
dow = str(input())

if (dow == 'Monday' or dow == 'Tuesday' or dow == 'Wednesday' or dow == 'Thursday' or dow == 'Friday' or\
        dow == 'Saturday') and 10 <= hour <= 18:
    print('open')
else:
    print('closed')
