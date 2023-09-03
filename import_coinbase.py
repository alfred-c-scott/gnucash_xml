import csv

trn_list = []

with open('private_csv/Coinbase-57e471d973edbf01338633d5-TransactionsHistoryReport-2023-09-03-16-04-34.csv', 'r') as csv_file:
    csv_data = csv_file.readlines()
    for ct, line in enumerate(csv_data):
        if line[0:9] == 'Timestamp':
            print('win')
            print(line[0:9])
            print(f'fields on line {ct+1}')
            fields_line = ct

cb_data = csv_data[fields_line:ct]
cb_data = csv.DictReader(cb_data)

for line in cb_data:
    print(line)
