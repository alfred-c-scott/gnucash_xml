import csv

trn_list = []

with open('private_csv/transfers-personal-FT72P9945347.csv', 'r') as csv_file:
    csv_data = csv.DictReader(csv_file)
    for row in csv_data:
        trn_list.append(row)

for trn in trn_list:
    print(trn)
