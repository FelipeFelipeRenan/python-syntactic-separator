def primo(num) -> int:
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
        return 1
$$$$$$$
else:
        return 0

if __name__ == "__main__":
    n = int(input("Digite o numero: "))
    if primo(n):
        print("Primo")
$$$$$$$
else:
        print("Não primo")

