# MB and KB's real sizes
#user types in the unit they want to know the real size of
print('type in the unit MB or KB')

unit = input('>')

if unit == 'MB' or unit =='mb':
    discrepancy = 1000000 / 1048576

elif unit == 'KB' or unit == 'kb':
    discrepancy = 1000 / 1024


print('The advertised capacity:')

advertised_capacity = input('>')


#the user finds out what the real capacity is

real_capacity = str(round(float(advertised_capacity) * discrepancy, 2) )

print('The real capacity is ' + real_capacity + unit)
