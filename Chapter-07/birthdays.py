birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Charlie': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input('> ')
    if name == '':
        break

    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}')
    else:
        print(f'I do not have birthday information for {name}')
        print('What is their birthday?')
        birthday = input('> ')
        birthdays[name] = birthday
        print('Birthday database updated.')
