"""
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object)
and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""


# My solution
def cakes(recipe, available):
    available_count = []
    for k in recipe.keys():
        if k in available:
            available_count.append(available[k] // recipe[k])
        else:
            return 0
    return min(available_count)


# Good solution
def cakes_good(recipe, available):
    try:
        return min(available[key] // recipe[key] for key in recipe)
    except:
        return 0


recipe_test = {'flour': 500, 'sugar': 200, 'eggs': 1}
recipe_test2 = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
available_test = {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}
available_test2 = {'sugar': 500, 'flour': 2000, 'milk': 2000}

print(cakes(recipe_test, available_test))
print(cakes(recipe_test2, available_test2))
print(cakes_good(recipe_test, available_test))
print(cakes_good(recipe_test2,available_test2))
