#!/bin/bash

mkdir saidas

touch saidas/saida1.py saidas/saida2.py saidas/saida3.py

echo -n > saidas/saida1.py > saidas/saida2.py  > saidas/saida3.py

python3 sep.py $1 >> saidas/saida1.py
python3 sep.py $2 >> saidas/saida2.py
python3 sep.py $3 >> saidas/saida3.py

bash ./csdiffV2.sh -s ": ( )" ./saidas/saida1.py ./saidas/saida2.py ./saidas/saida3.py 
