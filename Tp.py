x = int(input("Écris un nombre entier positif : "))
try:
    i = 2
    if x==1:
        raise ValueError("Non premier")
except ValueError:
    print("1 n'est pas un nombre premier")
else:
    while i < x and x % i != 0:
        i = i + 1
    if i == x:
        print("Le nombre", x, "est premier !")
    else:
        print("Ce n'est pas un nombre premier.")












