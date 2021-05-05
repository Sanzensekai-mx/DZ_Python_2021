# DZ_2

# Ex 1 FizzBuzz
def ex_1():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)


ex_1()

# Ex 2 Ключ-значение
dict_ = {'name': 'ivan', 'surname': 'ivanov'}  # {'ivan': 'name', 'ivanov': 'surname'}
print({v: k for k, v in dict_.items()})

# Ex 3 Дубликаты
list_ = [1, 1, 2, 3, 5, 4, 5, 5, 6]  # -> [1, 2, 3, 5, 4, 6]
print(list(set(list_)))
