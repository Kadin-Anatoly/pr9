import random

def generate_random_list():
    length = random.randint(1, 20)
    return [random.randint(1, 100) for i in range(length)]

def is_number(element):
    return isinstance(element, (int, float))

def are_all_elements_equal(numbers):
    for num in numbers:
        if num != numbers[0]:
            return False
    return True

def find_elements_greater_than_previous(numbers):
    for num in numbers:
        if not is_number(num):
            print(f"Ошибка: элемент {num} не является числом.")
            return

    if not numbers:
        print("Список пуст.")
        return

    if len(numbers) == 1:
        print("В списке только один элемент")
        return

    if are_all_elements_equal(numbers):
        print("Все элементы в списке одинаковые.")
        return

    print("Элементы, которые больше предыдущего:")
    if numbers[0] > numbers[-1]:
        print(numbers[0])

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            print(numbers[i])

random_list = generate_random_list()

print("Сгенерированный список:", random_list)

find_elements_greater_than_previous(random_list)