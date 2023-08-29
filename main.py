import json
import xmltodict

with open('a_c_s.gnucash', 'r') as gnucash_data:
    gnucash_data_dict = xmltodict.parse(gnucash_data.read())

gnucash_json = json.dumps(gnucash_data_dict, indent=4)

with open("data.json", "w") as json_file:
    json_file.write(gnucash_json)