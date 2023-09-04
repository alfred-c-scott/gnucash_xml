#!/usr/bin/python3


import os
from datetime import datetime
import csv


def xml_file_check(file_path):
    ti_c = os.path.getctime(file_path)
    ti_m = os.path.getmtime(file_path)

    with open('check_file.dat', 'r') as f:
        lst_mod = f.readline()
        print(lst_mod)
        print(str(ti_m))
        if lst_mod != str(ti_m):
            print('file changed')
            with open('check_file.dat', 'w') as write_f:
                write_f.write(str(ti_m))
                write_f.write('')
                write_f.close()
            f.close()
            return True
        else:
            print('file not changed')
            f.close()
            return False


def make_account_list(gnucash_data):
    account_list = []
    for account in gnucash_data["gnc-v2"]["gnc:book"]["gnc:account"]:
        account_dict = {"act_id": account["act:id"]["#text"], "act_name": account["act:name"]}
        account_list.append(account_dict.copy())

    # for account in account_list:
    #     print(account['act_id'])
    #     print(account['act_name'])

    return account_list


def make_transaction_list(gnucash_data, account_list):
    # print(account_list)
    transaction_list = []
    for trn in gnucash_data['gnc-v2']['gnc:book']['gnc:transaction']:
        # print(trn)
        splits_list = []
        for split in trn["trn:splits"]["trn:split"]:
            split_dict = {"split_id": split["split:id"]["#text"],
                          "split_val": split["split:value"],
                          "split_act_id": split["split:account"]["#text"]
                          }
            for account in account_list:
                if account["act_id"] == split_dict["split_act_id"]:
                    split_dict["split_act_name"] = account["act_name"]

            splits_list.append(split_dict.copy())

        trn_dict = {"trn_id": trn["trn:id"]["#text"],
                    "trn_posted": trn["trn:date-posted"]["ts:date"],
                    "trn_entered": trn["trn:date-entered"]["ts:date"],
                    "trn_description": trn["trn:description"],
                    "trn_splits": splits_list
                    }

        transaction_list.append(trn_dict.copy())
        # print(trn_dict)

    return transaction_list


def import_swan():
    trn_list = []
    with open('private_csv/transfers-personal-FT72P9945347.csv', 'r') as csv_file:
        swn_data = csv.DictReader(csv_file)

        for row in swn_data:
            trn_list.append(row)

    return trn_list


def import_coinbase():
    trn_list = []
    with open('private_csv/Coinbase-57e471d973edbf01338633d5-TransactionsHistoryReport-2023-09-03-16-04-34.csv',
              'r') as csv_file:
        csv_data = csv_file.readlines()
        for ct, line in enumerate(csv_data):
            if line[0:9] == 'Timestamp':
                fields_line = ct

        cb_data = csv_data[fields_line:ct]
        cb_data = csv.DictReader(cb_data)

    for trn in cb_data:
        # noinspection PyTypeChecker
        datetime_obj = datetime.fromisoformat(trn["Timestamp"].replace("Z", "+00:00"))
        epoch_time = datetime_obj.timestamp()
        print(epoch_time)
        print(type(epoch_time))
        # noinspection PyTypeChecker
        trn["Timestamp"] = int(epoch_time)
        trn_list.append(trn)

    return trn_list
