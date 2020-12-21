import re

file = open("input.txt")
lines = file.readlines()

ingredients_list = []
allergens_list = []
allergens_set = set()
ingredients_set = set()

for line in lines:
    [ingredients, allergens] = re.split(' \(contains',line)
    ingredients = ingredients.split(' ')
    ingredients_list += [ingredients]
    allergens = [val for val in re.split(' |,|\)|\n',allergens) if val != '']
    allergens_list += [allergens]
    for allergen in allergens:
        allergens_set.add(allergen)
    for ingredient in ingredients:
        ingredients_set.add(ingredient)

ALLERGEN_INGREDIENT_MAPPING = {}
#find common ingredients for each allergen
for allergen in allergens_set:
    candidate_ingredients = []
    for i,allergens in enumerate(allergens_list):
        if allergens.__contains__(allergen):
            candidate_ingredients += [ingredients_list[i]]
    common_ingredients = []
    for ingredient in ingredients_set:
        isCommon = True
        for ingredients in candidate_ingredients:
            if not ingredients.__contains__(ingredient):
                isCommon = False
                break
        if isCommon:
            common_ingredients += [ingredient]
    ALLERGEN_INGREDIENT_MAPPING[allergen] = common_ingredients

ingredients_with_allergens = []
while True:
    remove_ingredient = ""
    for key in ALLERGEN_INGREDIENT_MAPPING.keys():
        # find an allergen with just one entry
        if len(ALLERGEN_INGREDIENT_MAPPING.get(key)) == 1:
            remove_ingredient = ALLERGEN_INGREDIENT_MAPPING.pop(key)[0]
            print(key,remove_ingredient)
            ingredients_with_allergens += [remove_ingredient]
            break
    for key in ALLERGEN_INGREDIENT_MAPPING.keys():
        ing_list = ALLERGEN_INGREDIENT_MAPPING.get(key)
        if ing_list.__contains__(remove_ingredient):
            ing_list.remove(remove_ingredient)
            ALLERGEN_INGREDIENT_MAPPING.update({key:ing_list})
            if len(ALLERGEN_INGREDIENT_MAPPING) == 1:
                print(key,ing_list[0])
                ingredients_with_allergens += [ing_list[0]]
    if len(ALLERGEN_INGREDIENT_MAPPING) == 1:
        break

for ingredient in ingredients_with_allergens:
    ingredients_set.remove(ingredient)

cnt = 0
for ingredient in ingredients_set:
    for ingredients in ingredients_list:
        if ingredients.__contains__(ingredient):
            cnt += 1
print(cnt)