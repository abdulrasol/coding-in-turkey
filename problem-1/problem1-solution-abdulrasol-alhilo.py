# get ingredients and frige items from chef and store it as list after removing unwanted chars
indgrs = input('enter ingredients to cook something\nas tomato, onion, lettuce: ').replace(
    ' ', '').lstrip(',').rstrip(',').split(',')
fridge = input('enter things that availble in fridge same way before: ').replace(
    ' ', '').lstrip(',').rstrip(',').split(',')


def validateRecipe(fridge, ingredients):
    availableItem = False
    for item in indgrs:
        if item in fridge:
            availableItem = True
        else:
            availableItem = False
            break
    return availableItem


print(validateRecipe(fridge, indgrs))
