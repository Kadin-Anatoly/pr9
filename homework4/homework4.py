numbers = []

while True:
    user_input = input("Введите число (или 'end' для завершения): ")

    if user_input.lower() == 'end':
        break

    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Это не число, попробуйте снова.")

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Количество четных чисел: {even_count}")
print(f"Количество нечетных чисел: {odd_count}")
