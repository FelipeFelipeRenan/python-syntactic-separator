import re
import sys
file = sys.argv[1:].pop()


linhas = []
linhas2 = []

aux = 0
n = 0

numeroLinha = []
count = 0

with open(file, "r") as f, open("out.txt", "w+") as fAux:
    linhas = f.readlines()
    linhas2 = fAux.readlines()
    

    for count ,linha in enumerate(linhas):
        aux = n
        number = len(re.findall("[  ] ", linha))
        n =  len(re.findall("[ ]{3}[^aA-zA]|[aA-Zz]\n", linha))
        

        if(re.search("\(", linha)):
            linhasAux = re.sub("\(", "\n####(\n####\n", linha)
            if(re.search("\)", linhasAux)):
                linhasAux = re.sub("\)", "\n####)\n####\n", linhasAux)
                if(re.search(":\n", linhasAux)):
                    
                    linhasAux = re.sub(":\n", "\n####:\n####\n", linhasAux)
                    fAux.write(f"{linhasAux}")
                    continue
                
            fAux.write(f"{linhasAux}")        
            continue
    
        if n < aux:
            print(count)
            numeroLinha.append(count)

            linhaMaior = re.sub("[ ]{2,1000}[^aA-zZ]", "####" * n, linha )
     
            fAux.write(f"{linhaMaior}")
            continue
        fAux.write(f"{linha}")
    print(count)
