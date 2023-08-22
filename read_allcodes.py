import csv
import json

contry_Codes_list = []
with open("country-codes.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            code = int(row[1])
            contry_Codes_list.append(code)
        except ValueError:
            continue

with open("country_code.json", 'w') as fi:
    json_file = json.dumps(contry_Codes_list)
    fi.write(json_file)
