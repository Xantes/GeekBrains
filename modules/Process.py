

# import abc
# import modules.Equipment as eq


# class Process():

#     def __init__(self, point):
#         self.inner_menu = {'1': self.create_printer(),
#                            '2': self.create_scanner(
#         ), '3': self.create_copier(), '4': self.create_mfu()}
#         return self.inner_menu.get(point)

#     def create_printer(self):
#         manufacturer, model, expendables = input(
#             "Create printer msg 1 ").split()
#         return eq.Printer(manufacturer, model, expendables)

#     def create_scanner(self):
#         manufacturer, model, dpi = input(
#             "Create scanner msg 1 ").split()
#         return eq.Scanner(manufacturer, model, dpi)

#     def create_copier(self):
#         return eq.Copier(manufacturer, model, speed)

#     def create_mfu(self):
#         return eq.MFU(manufacturer, model, wireless)
