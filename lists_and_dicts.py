def run():
    my_list = [ 1, "Hello", True, 4.5 ]
    my_dict = { "firstname": "Juan", "lastname": "Salazar" }

    super_list = [
        { "firstname": "Camilo", "lastname": "Gañan" },
        { "firstname": "Antonio", "lastname": "Garcia" },
        { "firstname": "Maria", "lastname": "Castañeda" },
        { "firstname": "Milena", "lastname": "Arcila" },
        { "firstname": "Daniela", "lastname": "Rodriguez" },
    ]

    super_dict = {
        "natural_nums": [ 1, 2, 3, 4, 5 ],
        "integer_nums": [ -1, -2, 0, 1, 2],
        "floating_nums": [1.1, 1.2, 1.3, 1.4, 1.5]
    }

    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()