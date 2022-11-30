import json

INPUT_FILE = "input.csv"



     # TODO реализовать конвертер из csv в json


def to_csv_file(OUTPUT_FILE, headers_list, data , delimiter = "," ,new_line = "\n"):
    with open(OUTPUT_FILE, 'w+') as f:
        f.write(headers_list, delimiter)
            for i in data:
                with open(OUTPUT_FILE, 'w+') as f:
                    f.write(i, new_line)

print (to_csv_file())