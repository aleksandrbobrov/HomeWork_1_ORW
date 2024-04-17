def create_cook_book(file_path):
    cook_book = {}
    with open(file_path, 'r') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = file.readline().strip().split('|')
                ingredient_name = ingredient_info[0].strip()
                quantity = int(ingredient_info[1].strip())
                measure = ingredient_info[2].strip()
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
            # Пропускаем пустую строку между блюдами
            file.readline()  
    return cook_book

# Пример использования:
file_path = 'recipes.txt'  # Путь к файлу с рецептами
cook_book = create_cook_book(file_path)

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
            else:
                shop_list[ingredient_name]['quantity'] += quantity
    return shop_list

# Пример использования:
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
print(shop_list)