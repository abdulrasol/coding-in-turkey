# get fride items from user and store it as list after removing unwanted chars
fridge = input('input fridge item seperated by comma , as => banana, apple, milk: ').replace(
    ' ', '').lstrip(',').rstrip(',').split(',')

# get elemet that uset want to find it and store it as string after removing unwanted chars
elemnt = input('input element want to find it: ').lstrip(
).rstrip().lstrip(',').rstrip(',')


# the function that responceble to find the element
def whereIsMyFood(fridge, item):
    item_location = -1
    index = 0
    while index < len(fridge):
        if item == fridge[index]:
            item_location = fridge.index(fridge[index])
        index = index + 1
    print(item_location)


whereIsMyFood(fridge, elemnt)
