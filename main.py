import json
import xmltodict

with open('crypto_test.gnucash', 'r') as gnucash_data:
    gnucash_data_dict = xmltodict.parse(gnucash_data.read())

print(gnucash_data_dict['gnc-v2']['gnc:book']['gnc:transaction'])

for transaction in gnucash_data_dict['gnc-v2']['gnc:book']['gnc:transaction']:
    print(transaction)
    print(transaction['trn:id'])
    print(transaction['trn:currency'])
    print(transaction['trn:date-posted'])
    print(transaction['trn:date-entered'])
    print(transaction['trn:description'])
    print(transaction['trn:slots'])
    print(transaction['trn:splits'])

gnucash_json = json.dumps(gnucash_data_dict, indent=4)

with open("data.json", "w") as json_file:
    json_file.write(gnucash_json)
