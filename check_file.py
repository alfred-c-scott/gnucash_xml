#!/usr/bin/python3

import os
import time

path = '/home/mick/Nextcloud/gnucash/crypto_test.gnucash'

ti_c = os.path.getctime(path)
ti_m = os.path.getmtime(path)

# set to true if testing from terminal
# set to false in deployment
from_terminal = False

with open ('check_file.dat', 'r') as f:
    lst_mod = f.readline()
    if from_terminal:
        print(lst_mod)
        print(str(ti_m))
    if lst_mod != str(ti_m):
        if from_terminal:
            print('file changed')
        with open('check_file.dat', 'w') as write_f:
            write_f.write(str(ti_m))
            write_f.write('')
            write_f.close()
    else:
        print('file not changed')
    f.close()

if from_terminal:
    print(ti_c)
    print(ti_m)

    # Converting the time in seconds to a timestamp
    c_ti = time.ctime(ti_c)
    m_ti = time.ctime(ti_m)

    print(f"The file located at the path {path} was created at {c_ti} and was "
          f"last modified at {m_ti}")

