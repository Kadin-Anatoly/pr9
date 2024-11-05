import random


def generate_random_list():
    length = random.randint(1, 20)
    return [random.randint(1, 100) for _ in range(length)]


def is_number(element):
    return isinstance(element, (int, float))


def are_all_elements_equal(numbers):
    for num in numbers:
        if num != numbers[0]:
            return False
    return True


def cyclic_shift_right(numbers):
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

    last_element = numbers[-1]
    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i - 1]
    numbers[0] = last_element

    print("Список после циклического сдвига вправо:", numbers)


random_list = generate_random_list()

print("Сгенерированный список:", random_list)

cyclic_shift_right(random_list)
