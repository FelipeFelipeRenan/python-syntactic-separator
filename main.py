import re

file = "teste.py"
linhas = []
linhas2 = []

aux = 0
n = 0

with open(file, "r") as f, open("out.txt", "w+") as fAux:
    linhas = f.readlines()
    linhas2 = fAux.readlines()

    for linha in linhas:
        aux = n
        number = len(re.findall("[  ] ", linha))
        n =  len(re.findall("[ ]{3}[^aA-zA]|[aA-Zz]\n", linha))
        if n >= aux:

            linhaMaior = re.sub("[ ]{2,1000}[^aA-zZ]|\([aA-zZ]\)\n", "####\n" * n, linha )
     
            fAux.write(f"{linhaMaior}")
            continue
        fAux.write(f"{linha}")
    
    for linha in linhas2:
        
        linhasAux = re.sub("\([aA-zZ]{0,100}", "####\n", linha)
        fAux.write(f"{linhasAux}")
    
    for linha in linhas2:
        
        linhasAux = re.sub("[aA-zZ]{0,100}\)", "####\n", linha)
        fAux.write(f"{linhasAux}")

#[ ]{2,1000}[^aA-zA]|[aA-Zz]\n
#[ ]{2,1000}[^aA-zZ]|[$aA-zZ]: