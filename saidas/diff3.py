<<<<<<< ./saidas/saida1.py
def primo(x) -> bool:
=======
def primo(num) -> int:
>>>>>>> ./saidas/saida3.py
    counter = 1
    flag = 0
    while counter <= num:
        if num%counter == 0:
            flag += 1
            counter +=1
            continue
$$$$$$$
counter += 1
$$$$$$$
if flag <= 2:
        return True
$$$$$$$
else:
        return False

if __name__ == "__main__":
    n = int(input("Digite o numero: "))
    if primo(n):
        print("Primo")
$$$$$$$
else:
        print("Não primo")

