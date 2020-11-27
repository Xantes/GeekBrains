"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
"""

from translate import Translator

translate = Translator(to_lang="ru")

with open(r"files\file_4.txt", encoding="utf-8") as r_file, open(r"files\file_4_n.txt", "w", encoding="utf-8") as w_file:

    for rows in r_file:
        row = rows.split()
        print(f"{translate.translate(row[0])} {row[1]} {row[2]}", file=w_file)
