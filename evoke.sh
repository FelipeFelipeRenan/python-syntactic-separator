
touch saida1.py saida2.py saida3.py
echo -n > saida1.py > saida2.py  > saida3.py

python3 sep.py $1 >> saida1.py
python3 sep.py $2 >> saida2.py
python3 sep.py $3 >> saida3.py