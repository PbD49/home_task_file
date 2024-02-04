def read_cook_book(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = file.readline().split('|')
                ingredient_name = ingredient_info[0].strip()
                quantity = int(ingredient_info[1].strip())
                measure = ingredient_info[2].strip()
                ingredient = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            file.readline()  # empty line between dishes
    return cook_book


file_name = 'recipes.txt'  # замените 'recipes.txt' на имя вашего файла
cook_book = read_cook_book(file_name)
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}

    result_shop_list = {}
    for key, value in shop_list.items():
        result_shop_list[key] = {'measure': value['measure'], 'quantity': value['quantity']}
    return result_shop_list


dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)
print(shop_list)


def merge_files(file_names, output_file):
    file_data = []
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = file.readlines()
            file_data.append((file_name, len(data), data))

    file_data.sort(key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as file:
        for name, length, data in file_data:
            file.write(f"{name}\n{length}\n")
            file.writelines([f"{line}" for line in data])
            file.write('\n')


file_names = ['1.txt', '2.txt', '3.txt']  # замените это на фактические имена ваших файлов
output_file = 'result.txt'  # имя итогового файла
merge_files(file_names, output_file)