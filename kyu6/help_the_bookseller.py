def stock_list(list_of_art, list_of_cat):
    if not list_of_art or not list_of_cat:
        return ""

    quantity_by_category = dict.fromkeys(list_of_cat, 0)
    for art in list_of_art:
        if art[0] in quantity_by_category:
            quantity_by_category[art[0]] += int(art.split()[-1])

    result = []
    for key, value in quantity_by_category.items():
        result.append(f"({key} : {value})")
    return ' - '.join(result)
