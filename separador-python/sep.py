import re
import sys

file1 = sys.argv[1:].pop()


## files = [file1,file2, file3]

linhas = []
linhas_aux = []
linhas1 = []
linhas2 = []
linhas3 = []

output = []

aux = 0
n = 0

numeroLinha = []
count = 0


with open( file1, "r") as f, open("out.py", "w+") as fAux: 
    linhas = f.readlines()
    linhas1 = fAux.readlines()

    for count ,linha in enumerate(linhas):
        aux = n
        number = len(re.findall("[  ] ", linha))
        n =  len(re.findall("[ ]{3}[^aA-zZ]|[aA-Zz]\n", linha))

        if n < aux:
            
            numeroLinha.append(count)
            linhaMaior = re.sub("[ ]{2,1000}[^aA-zZ]", "$$$$$$$\n", linha )
 
            fAux.write(f"{linhaMaior}")
            print(linhaMaior, end="")
            continue
        fAux.write(f"{linha}")
        print(linha, end="")

    
    
        

'''
linhas.clear()
with open(file2, "r") as f2, open("out2.py", "w+") as fAux2:
    linhas = f2.readlines()
    linhas2 = fAux2.readlines()

    for count ,linha in enumerate(linhas):
        aux = n
        number = len(re.findall("[  ] ", linha))
        n =  len(re.findall("[ ]{3}[^aA-zA]|[aA-Zz]\n", linha))

        if n < aux:
            print(count)
            numeroLinha.append(count)
            linhaMaior = re.sub("[ ]{2,1000}[^aA-zZ]", "####" * n, linha )
 
            fAux2.write(f"{linhaMaior}")
            continue
        fAux2.write(f"{linha}")
    fAux2.close()


linhas.clear()
with open(file3, "r") as f3, open("out3.py", "w+") as fAux3:
    linhas = f3.readlines()
    linhas3 = fAux3.readlines()

    for count ,linha in enumerate(linhas):
        aux = n
        number = len(re.findall("[  ] ", linha))
        n =  len(re.findall("[ ]{3}[^aA-zA]|[aA-Zz]\n", linha))

        if n < aux:
            print(count)
            numeroLinha.append(count)
            linhaMaior = re.sub("[ ]{2,1000}[^aA-zZ]", "####" * n, linha )
 
            fAux3.write(f"{linhaMaior}")
            continue
        fAux3.write(f"{linha}")
    fAux3.close()        

        
'''