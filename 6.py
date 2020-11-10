def int_func(args: str):
    for arg in args:
        if ch_letter(arg):
            print(arg.capitalize())
    return


def ch_letter(word):
    for letter in word:
        if ord(letter) not in range(97, 133):
            return False
    return True


var_input = str(input("Введите слова разделенные пробелом: "))
var_input = var_input.replace('  ', ' ')
var_input = var_input.split()

int_func(var_input)
