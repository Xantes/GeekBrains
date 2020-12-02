import modules.Documentation as doc
import modules.Equipment as eq
import modules.Structure as st

workplace = st.Workplace('112 Room', 'Albert Hoffman')
print(workplace)

printer = eq.Printer('Hp', '1022', 'q2612a')
print(printer)
print(printer.work_please(10))
printer.receive_equipment(2)

scanner = eq.Scanner('Cannon', 'MF50', 300)
print(scanner)
print(scanner.work_please(3))
scanner.receive_equipment(4)
scanner.issue_equipment(workplace, 1)
