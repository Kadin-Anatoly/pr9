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

odd_list = []
for num in numbers:
    if num % 2 != 0:
        odd_list.append(num)
print(odd_list)
