import re

file = "teste.py"
linhas = []
aux = 0

with open(file, "r") as f:
    linhas = f.readlines()
    number = 0
    for linha in linhas:
        number = len(re.findall("[  ] ", linha))
        n =  len(re.findall("[ ]{3}[^aA-zA]|[aA-Zz]\n", linha))
        print(re.sub("[ ]{2,1000}[^aA-zA]|[aA-Zz]\n", "#####" * n, linha ))
        print(len(re.findall("[ ]{3}[^aA-zA]|[aA-Zz]\n", linha)))
        
        aux += 1



#[ ]{2,1000}[^aA-zA]|[aA-Zz]\n