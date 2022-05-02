
lists = []
with open('lists/listOfList.txt') as lol:
    for index, l in enumerate(lol):
        lists.append(l)
        lists[index] = lists[index][:-1]

if lists:
    print('Open which list')
    print(lists)
else:
    q = input('Would you like to create a list? \n> ')

    if q.lower() == 'yes':
        q = input('Lists Name? \n> ')
        file = open(f'lists/{q}.txt', 'x')
        with open('lists/listOfList.txt', 'w') as file:
            file.write(f'{q}\n')
    elif q.lower() == 'no':
        pass