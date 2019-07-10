#!/bin/bash

# wrapper script for the python script sbook.py

cd $(dirname $0)

# just use the python script like this
python ./sbook.py -d my_sbook_data_contacts.txt -d my_sbook_data_passwords.txt $@


