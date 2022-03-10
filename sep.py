import re
import sys

file1 = sys.argv[1:].pop()
file2 = sys.argv[2:].pop()
file3 = sys.argv[3:].pop()

files = [file1,file2, file3]

linhas = []
linhas2 = []

aux = 0
n = 0

numeroLinha = []
count = 0
for file in files:
    with open(file, "r") as f, open("out.txt", "w+") as fAux:
        linhas = f.readlines()
        linhas2 = fAux.readlines()
    

        for count ,linha in enumerate(linhas):
            aux = n
            number = len(re.findall("[  ] ", linha))
            n =  len(re.findall("[ ]{3}[^aA-zA]|[aA-Zz]\n", linha))

    
            if n < aux:
                print(count)
                numeroLinha.append(count)

                linhaMaior = re.sub("[ ]{2,1000}[^aA-zZ]", "####" * n, linha )
     
                fAux.write(f"{linhaMaior}")
                continue
            fAux.write(f"{linha}")
print(count)


        
