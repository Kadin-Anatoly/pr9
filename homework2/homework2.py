import math
def get_integer_squares(a, b):

    start = min(a, b)
    end = max(a, b)

    if start.is_integer() and end.is_integer():
        start = int(start) + 1
        end = int(end) - 1
    else:
        start = math.ceil(start)
        end = math.floor(end)

    squares = [i ** 2 for i in range(start, end + 1)]
    return squares

def main():
    while True:
        try:
            a = float(input("Введите число a: "))
            b = float(input("Введите число b: "))
            break
        except ValueError:
            print("Ошибка: пожалуйста, введите корректные числа.")

    squares = get_integer_squares(a, b)

    print("Список квадратов целых чисел между a и b:", squares)

if __name__ == "__main__":
    main()
