import re
import os

file = "teste.py"
linhas = []
linhas2 = []

aux = 0
n = 0

with open(file, "r") as f, open("out.txt", "a+") as fAux:
    linhas = f.readlines()
    linhas2 = fAux.readlines()

    for linha in linhas:
        aux = n
        number = len(re.findall("[  ] ", linha))
        n =  len(re.findall("[ ]{3}[^aA-zA]|[aA-Zz]\n", linha))
        if n > aux:
            linhaMaior = re.sub("[ ]{2,1000}[^aA-zA]|[aA-Zz]\n", "#####" * n, linha )
            fAux.write(f"{linhaMaior}")
            continue
        #print(len(re.findall("[ ]{3}[^aA-zA]|[aA-Zz]\n", linha)))
        fAux.write(f"{linha}")

#[ ]{2,1000}[^aA-zA]|[aA-Zz]\n