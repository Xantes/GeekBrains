max_digit = 0

input_var = int(input("Введите целое положительное число: "))

if input_var >= 0:
    while input_var != 0:
        if max_digit <= input_var % 10:
            max_digit = input_var % 10
        input_var = input_var // 10

print(f"Самое большая цифра во введенном числе: {max_digit}")
