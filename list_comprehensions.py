def run():
    # Esto es un ejemplo de una list comprehension
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    # for i in range(1, 101):
    #     squares.append(i**2) 

    # for i in range(1, 101):
    #     if i % 3 == 0:
    #         squares.append(i)
    reto = [i for i in range(1, 10000) if i % 36 == 0]

    print(reto)

if __name__ == '__main__':
    run()