# get ingredients and frige items from chef and store it as list after removing unwanted chars
arg1 = input("enter ingredients to cook something as tomato: 1, onion: 2\ningredients : ").replace(
    ' ', '').lstrip(',').rstrip(',').split(',')
arg2 = input('enter things that availble in fridge same way before\nfridge items : ').replace(
    ' ', '').lstrip(',').rstrip(',').split(',')

# create empty list to store data and quantity in it.
indgrs = {}
fridge = {}

# parse data into python dict
try:
    for i in arg1:
        indgrs[i.split(':')[0].lstrip('"')] = int(i.split(':')[1].rstrip('"'))
    for i in arg2:
        fridge[i.split(':')[0].lstrip('"')] = int(i.split(':')[1].rstrip('"'))
except:
    print(' input shoud be as tomato: 1, onion: 2 format')

# checking function


def validateRecipeWithQuantity(fridge, ingredients):
    availableItem = False
    for item in indgrs:
        if indgrs[item] <= fridge[item]:
            availableItem = True
        else:
            availableItem = False
            break
    return availableItem


print(validateRecipeWithQuantity(fridge, indgrs))
