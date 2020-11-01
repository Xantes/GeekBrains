input_var = int(input("Введите целое положительное число: "))

var1 = input_var
var2 = str(input_var) + str(input_var)
var3 = str(input_var) + str(input_var) + str(input_var)

result = int(var1) + int(var2) + int(var3)

print(f"{result}")
