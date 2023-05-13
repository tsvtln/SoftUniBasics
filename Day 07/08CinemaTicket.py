dow = str(input())

if dow == 'Monday' or dow == 'Tuesday' or dow == 'Friday':
    print('12')
elif dow == 'Wednesday' or dow == 'Thursday':
    print('14')
elif dow == 'Saturday' or dow == 'Sunday':
    print('16')