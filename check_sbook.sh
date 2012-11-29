#!/bin/bash
set -x

# check_sbook.sh
# non regression test of the script sbook.py

TMP_DIR=/tmp

cat <<_DIRECTORY_1 > $TMP_DIR/directory_1.txt
# /tmp/directory_1.txt

robert dupont # no comment
27/05/1980
ardenne/president de la chambre d'agriculture
01 35 85 21 14

thierry roland
agriculteur
# visible ou invisible


robert thierry
agriculteur
12/09/2001
# attention ca compte comme separation
miriame soleil
05/01/1990
agricultrice
_DIRECTORY_1

cat <<_DIRECTORY_2 > $TMP_DIR/directory_2.txt
roberto dupont
27/12/1980
marne/president de la chambre d'agriculture
03 95 85 21 14

daniel roland
heliculteur


david thierry
apiculteur
12/09/2001

mireille soleil
05/01/1960
agricultrice
_DIRECTORY_2

echo -e "\n\n\n ### Begin of the non regression test of sbook.py ###\n\n\n"


echo "Which paragraphs contain robert in the file directory_1.txt ?"
sbook.py -d $TMP_DIR/directory_1.txt robert

echo "Which paragraphs contain robert in the file directory_1.txt and directory_2.txt ?"
sbook.py -d $TMP_DIR/directory_1.txt -d $TMP_DIR/directory_2.txt robert

echo "Which contain robert AND thierry ?"
sbook.py -d $TMP_DIR/directory_1.txt -d $TMP_DIR/directory_2.txt robert thierry

echo "Which contain rob OR rol ?"
sbook.py -d $TMP_DIR/directory_1.txt -d $TMP_DIR/directory_2.txt rob\|rol

echo "Which contain (rob OR rol) AND thierry ?"
sbook.py -d $TMP_DIR/directory_1.txt -d $TMP_DIR/directory_2.txt rob\|rol thierry

echo "The arguments of -g have the same meaning of the script arguments."
sbook.py -d $TMP_DIR/directory_1.txt -d $TMP_DIR/directory_2.txt -g rob\|rol -g thierry

echo "Which contain (rob OR rol) but NOT thierry ?"
sbook.py -d $TMP_DIR/directory_1.txt -d $TMP_DIR/directory_2.txt -g rob\|rol -v thierry

echo "Add the data file name to know where data come from."
sbook.py -d $TMP_DIR/directory_1.txt -d $TMP_DIR/directory_2.txt -g rob\|rol -v thierry -a

echo "end of check_sbook.sh"


