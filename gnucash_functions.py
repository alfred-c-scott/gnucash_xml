# gnucash_functions.py

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
