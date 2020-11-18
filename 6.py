import re
try:
    with open(r"files\file_6.txt", encoding="utf-8") as r_file:
        print({array.split()[0]: sum(list(int(val) for val in list(map(lambda x: re.sub(r'[^\d]', '', x), array.split()[1::])) if val))
               for array in r_file.readlines()})
except Exception as e:
    print(e)
