fridge = input('input fridge item seperated by comma , as => banana, apple, milk: ').replace(' ','').split(',')
elemnt = input('input element want to find it: ').lstrip().rstrip()
def whereIsMyFood(fridge, item):
    item_location = -1
    index = 0
    while index < len(fridge):
        if item == fridge[index]:
            item_location = fridge.index(fridge[index])
        index = index + 1
    print(item_location)

whereIsMyFood(fridge,elemnt)