# Creer deux programme avec la boucle for et la boucle while qui affiche les 100 premiers nombres entiers premiers.

# Avec la boucle for : 

#Lire la saisie de l'utilisateur
min = int(input("Entrez le min : "))
max = int(input("Entrez le max : "))

for n in range(min,max + 1):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                break
        else:
            print(n)

#  Avec la boucle while : 

print("Les 100 premiers nombres premiers sont : ")

n_premier = 1
i = 2

while n_premier < 100 :
    j = 2
    nombre_trouve = False
    while (j <= i // 2) and (nombre_trouve == False):
        if i % j == 0:
            nombre_trouve = True
        else:
            j += 1
    if nombre_trouve == False:
        print(n_premier, i)
        n_premier += 1
    i += 1