class done(Exception):
    pass


marketBasket = {}


def menu(option):
    if option == 1:
        add()
    elif option == 2:
        delItem()
    elif option == 3:
        showBasketContent()
    elif option == 4:
        searchItem()
    elif option == 0:
        raise done
    else:
        print('Eror: Enter a number between 0 and 4.')


def help():
    print(""" 
              1. Add item
              2. Del item
              3. Show basket contant
              4. Search item
              0. Exit
              """)


def add():
    item = input('Enter item: ')
    qty = int(input('Enter Qty: '))
    if item in marketBasket.keys():
        marketBasket[item] += qty
    else:
        marketBasket[item] = qty


def delItem():

    item = input('Enter item to remove frome market basket: ')
    print(f'Do you want to delet all the {item}s? ')
    yesOrNo = input('Enter your answer: (Yes/No): ')
    if yesOrNo == 'No' or yesOrNo == 'no' or yesOrNo == 'N':
        qty = int(input(
            f'how many of {item} do you want to remove from your basket? (Enter a number): '))
        marketBasket[item] -= qty
    else:

        marketBasket.pop(item, "Eror: this item dose't exist. ")


def showBasketContent():
    print('show baskets content:')
    print('*'*30)
    print(' '*30)
    for key in marketBasket.keys():
        print(key, ' : ', marketBasket[key])
        print(' '*30)
        print('*'*30)


def searchItem():
    item = int(input('Enter item to search in market basket: '))
    if item in marketBasket.keys():
        print('found')
    else:
        print('not found')


try:
    while True:
        help()
        option = int(input('Enter option (0-4): '))
        menu(option)
except done:
    print('sarabada!')
