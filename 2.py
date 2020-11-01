input_var = int(input("Введите время в секундах: "))

hours = input_var // 3600
seconds = input_var % 60
minutes = input_var % 3600 // 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")
