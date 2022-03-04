def show_shop(number, shop):
    print(f'\n\t {number} магазин \t\n')
    for type_products, products in shop.items():
        print(f'{type_products}: {products}')


shopProducts1 = {
    'Fish': {'Burbot', 'Bream', 'Eel', 'Carp'},
    'Berries': {'Cherry', 'Currant', 'Watermelon', 'Cranberry'},
    'Fruits': {'Apple', 'Banana', 'Orange', 'Lemon', 'Avocado'},
    'Vegetables': {'Cucumber', 'Potato', 'Tomato', 'Cabbage', 'Carrot'},
    'Nuts': {'Walnut', 'Almond', 'Peanut', 'Brazil nut', 'Hazelnut'},
    'Meat products': {'Beef', 'Pork', 'Chicken', 'Veal', 'Mutton'},
    'Dairy products': {'Milk', 'Butter', 'Cheese', 'Cream', 'Ice cream'}
}

shopProducts2 = {
    'Berries': {'Cherry', 'Currant', 'Watermelon'},
    'Fruits': {'Pineapple', 'Apricot', 'Banana', 'Lemon'},
    'Vegetables': {'Radish', 'Onion', 'Potato', 'Cabbage'},
    'Meat products': {'Beef', 'Chicken', 'Veal'},
    'Dairy products': {'Milk', 'Cheese', 'Cream'}
}

shopProducts3 = dict()

# Множество для выборки уникальных ключей из первых двух словарей.
categories = set(set(shopProducts1.keys()) & set(shopProducts2.keys()))

for category in categories:
    shopProducts3[category] = set(shopProducts1.get(category)) | \
                              set(shopProducts2.get(category))

show_shop(1, shopProducts1)
show_shop(2, shopProducts2)
show_shop(3, shopProducts3)
