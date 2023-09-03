import json
import xmltodict

from gnucash_functions import make_account_list, make_transaction_list, xml_file_check, import_swan, import_coinbase

gnucash_xml_path = '/home/mick/Nextcloud/gnucash/crypto_test.gnucash'

from_terminal = False

with open('crypto_test.gnucash', 'r') as gnucash_data:
    gnucash_xml_dict = xmltodict.parse(gnucash_data.read())
    gnucash_data.close()

if from_terminal:
    print(gnucash_xml_dict['gnc-v2']['gnc:book']['gnc:transaction'])
    print(gnucash_xml_dict['gnc-v2']['gnc:book']['gnc:account'])

act_list = make_account_list(gnucash_xml_dict)
trn_list = make_transaction_list(gnucash_xml_dict, act_list)
swn_data = import_swan()
cb_data = import_coinbase()

act_dict = {"gnucash_accounts": act_list}
trn_dict = {"gnucash_transactions": trn_list}
swn_dict = {"swan_btc_transactions": swn_data}
cb_dict = {"coinbase_transactions": cb_data}

gnucash_json = json.dumps(gnucash_xml_dict, indent=2)
with open('private_json/gnucash_xml.json', 'w') as json_file:
    json_file.write(gnucash_json)
    json_file.close()

act_json = json.dumps(act_dict, indent=2)
with open('private_json/act.json', 'w') as json_file:
    json_file.write(act_json)
    json_file.close()

trn_json = json.dumps(trn_dict, indent=2)
with open('private_json/trn.json', 'w') as json_file:
    json_file.write(trn_json)
    json_file.close()

swn_json = json.dumps(swn_dict, indent=2)
with open('private_json/swn.json', 'w') as json_file:
    json_file.write(swn_json)
    json_file.close()

cb_json = json.dumps(cb_dict, indent=2)
with open('private_json/cb.json', 'w') as json_file:
    json_file.write(cb_json)
    json_file.close()
    
    
payload = {}
payload["gnucash_xml"] = gnucash_xml_dict["gnc-v2"]
print(payload["gnucash_xml"])
payload["gnucash_act_list"] = act_dict["gnucash_accounts"]
print(payload["gnucash_act_list"])
payload["gnucash_trn_list"] = trn_dict["gnucash_transactions"]
print(payload["gnucash_trn_list"])
payload["swn_trn_list"] = swn_dict["swan_btc_transactions"]
print(payload["swn_trn_list"])
payload["cb_trn_list"] = cb_dict["coinbase_transactions"]
print(payload["cb_trn_list"])
