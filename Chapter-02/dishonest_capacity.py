print('Enter TB or GB for the advertised unit:')
unit = input('>').upper()

# Calculate the amount that the advertised capacity lies:
if unit == 'TB':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB':
    discrepancy = 1000000000 / 1073741824
else:
    print('Invalid unit. Please enter TB or GB.')
    exit()

print('Enter the advertised capacity:')
advertised_capacity = float(input('>'))

# Calculate the real capacity, round it to the nearest hundredths,
# and convert it to a string so it can be concatenated:
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print(f'The actual capacity is {real_capacity} {unit}')
