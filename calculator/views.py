from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def print_recipe(request, name):
    number_of_servings = int(request.GET.get('servings', 1))
    recipe = name
    ingredients = DATA.get(recipe, {})
    calculated_ingredients = {}
    for ingredient, amount in ingredients.items():
        calculated_ingredients[ingredient] = amount * number_of_servings
    context = {'recipe': calculated_ingredients}

    return render(request, 'calculator/index.html', context)
