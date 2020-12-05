import modules.Documentation as doc
import modules.Equipment as eq
import modules.Structure as st
import modules.Process as pr

menu_text = 'Msg 1: \nMsq 2: \nMsg 3: \nMsg 4: \n'

while False:
    answer = str(input(menu_text))
    if answer == ':q':
        break
    if answer == '1':
        manufacturer = input("Manufacturer: ")
        model = input('Model: ')
        expendables = input('Expendables: ')
        printer = eq.Printer(manufacturer, model, expendables)
        counts = input('Counts: ')
        printer.receive_equipment(counts)
        break
    if answer == '2':
        pass
    if answer == '3':
        pass
    if answer == '4':
        pass


# workplace = st.Workplace('112 Room', 'Albert Hoffman')
# print(workplace)
# # printer = eq.Printer('Hp', '1022', 'q2612a')
# print(printer)
# print(printer.work_please(10))
# # printer.receive_equipment(2)

# scanner = eq.Scanner('Cannon', 'MF50', 300)
# print(scanner)
# print(scanner.work_please(3))
# scanner.receive_equipment(4)
# scanner.issue_equipment(workplace, 1)

print(eq.Equipment.check_storage())
