def cakes(recipe, available):
    quantity = float('inf')

    for key, value in recipe.items():
        available_value = available.get(key, 0)
        if available_value:
            quantity = min(available_value // value, quantity)
        else:
            return available_value

    return quantity
