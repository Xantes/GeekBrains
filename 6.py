start_distance = float(input("Введите пройденную дистанцию в первый день: "))
final_distance = float(input("Введите желаемую дистанцию: "))

grow_percent = 0.1
days = 1

while start_distance < final_distance:
    start_distance = start_distance + (start_distance * grow_percent)
    days += 1

print(f"На {days}-й спортсмен достиг результата - не менее {final_distance:.0f} км")
