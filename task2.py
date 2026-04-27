def find_top_seller(products: dict, sales: dict) -> str:
    for product, sale, key in zip(products.values(), sales.values(), products.keys()):        
        tushum = product * sale
        temp = 0
        if temp < tushum:
            temp = tushum
    return key


print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10,   "Banan": 5,    "Uzum": 8}
))