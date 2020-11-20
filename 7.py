import json

array = []

try:
    with open("files\\file_7.txt", encoding="utf-8") as r_file, open("files\\file_7_n.txt", "w", encoding="utf-8") as w_file:
        array.append({lines.split()[0]: float(lines.split()[2]) -
                      float(lines.split()[3]) for lines in r_file})
        r_file.seek(0)
        array.append({'average_profit':
                      sum([float(el.split()[2]) - float(el.split()[3]) for el in r_file if float(el.split()[2]) > float(el.split()[3])])})

        print(json.dumps(array, sort_keys=True, indent=4), file=w_file)


except Exception as e:
    print(e)
