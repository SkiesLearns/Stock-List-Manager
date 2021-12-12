def showStock(f):
    print(f.read())
    userDecide = input("""
To add items to your stock list please type 'ADD'
To remove items from your stock please type 'REMOVE'
To close application type 'CLOSE'
: """)
    if userDecide.lower() == 'add':
        addStock(f)
    elif userDecide.lower() == 'remove':
        delStock(f)
    elif userDecide.lower() == 'close':
        print('Closing...')
        exit()
    else:
        print('Response does not match criteria.')

def addStock(f):
    item_add = input("""
Please enter the name of the item you wish to add.
: """)
    f.write(item_add+' : ')
    quantityItem = input("""
Item added, please enter the current quantity for the item.
: """)
    f.write(quantityItem+'\n')
    userDecide = input("""
Quantity added. Info will be saved on close. If you need to;
If you need to add more items type 'ADD'
If you need to delete items type 'REMOVE'
If you would like to exit application type 'CLOSE'
: """)
    if userDecide.lower() == 'add':
        addStock(f)
    elif userDecide.lower() == 'remove':
        delStock(f)
    elif userDecide.lower() == 'close':
        print('Closing...')
        exit()
    else:
        print('Response does not match criteria.')
    exit()

def delStock(f):
    count = 0
    itemRemove = input("""
Please enter the item you wish to delete.
: """)
    with open("CurrentStock.txt", "r") as f:
        lines = f.readlines()
    with open('CurrentStock.txt', "w") as f:
        for line in lines:
            if itemRemove not in line:
                f.write(line)
    userDecide = input("""
Items removed from list. When closed info will update.
If you need to add more items type 'ADD'
If you need to delete items type 'REMOVE'
If you would like to exit application type 'CLOSE'
: """)
    if userDecide.lower() == 'add':
        addStock(f)
    elif userDecide.lower() == 'remove':
        delStock(f)
    elif userDecide.lower() == 'close':
        print('Closing...')
        exit()
    else:
        print('Response does not match criteria.')
    exit()


with open('CurrentStock.txt', 'r+') as f:
    print("""
=====================================================
        Welcome to Max's stock project.
=====================================================

Current stock:
""")

    showStock(f)

