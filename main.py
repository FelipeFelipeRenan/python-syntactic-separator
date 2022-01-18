import re
import os

file = "teste.py"
linhas = []
aux = 0
n = 0

fileAux = open("out.txt", "a+")


with open(file, "r") as f:
    linhas = f.readlines()

    for linha in linhas:
        aux = n
        number = len(re.findall("[  ] ", linha))
        n =  len(re.findall("[ ]{3}[^aA-zA]|[aA-Zz]\n", linha))
        if n > aux:
            print(re.sub("[ ]{2,1000}[^aA-zA]|[aA-Zz]\n", "#####" * n, linha ), aux)
        #print(len(re.findall("[ ]{3}[^aA-zA]|[aA-Zz]\n", linha)))
        

#[ ]{2,1000}[^aA-zA]|[aA-Zz]\n