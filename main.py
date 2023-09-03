import json
import xmltodict

from gnucash_functions import make_account_list, make_transaction_list, xml_file_check

gnucash_xml_path = '/home/mick/Nextcloud/gnucash/crypto_test.gnucash'

from_terminal = True

with open('crypto_test.gnucash', 'r') as gnucash_data:
    gnucash_data_dict = xmltodict.parse(gnucash_data.read())
    gnucash_data.close()

if from_terminal:
    print(gnucash_data_dict['gnc-v2']['gnc:book']['gnc:transaction'])
    print(gnucash_data_dict['gnc-v2']['gnc:book']['gnc:account'])

trans_account_id_list = []
act_list = make_account_list(gnucash_data_dict)
transaction_list = make_transaction_list(gnucash_data_dict, act_list)

for trn in transaction_list:
    print(trn)

gnucash_json = json.dumps(gnucash_data_dict, indent=4)

with open("data.json", "w") as json_file:
    json_file.write(gnucash_json)
