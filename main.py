from random import randint

#creer une liste qui regroupe les 3 choix possibles
t = ["Pierre", "Papier", "Ciseaux"]

#l'ordinateur choisit une option dans la liste
computer = t[randint(0,2)]
scorecomp = 0
scorehuman = 0
print("Jeu pierre-papier-ciseaux en 5 manches")

#on cree un boucle for, qui va nous permettre de jouer 5 manches
for i in range(5):

#ici le joueur doit ecrire le geste qu'il souhaite choisir
    jeu = input("Veuillez indiquez votre choix\n")
    if jeu == "Pierre":
        if computer == jeu:
            print("Egalite")
        elif computer == "Papier":
            print("Vous avez perdu")
            print("L'ordinateur a choisi " + computer)
            scorecomp += 1
            print("Ordinateur = " + str(scorecomp) + "\nHumain = " + str(scorehuman))
        elif computer == "Ciseaux":
            print("Vous avez gagné")
            print("L'ordinateur a choisi " + computer)
            scorehuman += 1
            print("Ordinateur = " + str(scorecomp) + "\nHumain = " + str(scorehuman))
#dans le cas ou le joueur ecrit n'importe quoi
        else:
            print("N'essayez pas de me duper")
            print("Point de penalite")
            scorecomp += 1
            print("Ordinateur = " + str(scorecomp) + "\nHumain = " + str(scorehuman))
    if jeu == "Papier":
        if computer == jeu:
            print("Egalite")
        elif computer == "Ciseaux":
            print("Vous avez perdu")
            print("L'ordinateur a choisi " + computer)
            scorecomp += 1
            print("Ordinateur = " + str(scorecomp) + "\nHumain = " + str(scorehuman))
        elif computer == "Pierre":
            print("Vous avez gagné")
            print("L'ordinateur a choisi " + computer)
            scorehuman += 1
            print("Ordinateur = " + str(scorecomp) + "\nHumain = " + str(scorehuman))
    if jeu == "Ciseaux":
        if computer == jeu:
            print("Egalite")
        elif computer == "Pierre":
            print("Vous avez perdu")
            print("L'ordinateur a choisi " + computer)
            scorecomp += 1
            print("Ordinateur = " + str(scorecomp) + "\nHumain = " + str(scorehuman))
        elif computer == "Papier":
            print("Vous avez gagné")
            print("L'ordinateur a choisi " + computer)
            scorehuman += 1
            print("Ordinateur = " + str(scorecomp) + "\nHumain = " + str(scorehuman))
    if jeu != "Papier" or "Pierre" or "Ciseaux":
            print("N'essayez pas de me duper")
            print("Point de penalite")
            scorecomp += 1
            print("Ordinateur = " + str(scorecomp) + "\nHumain = " + str(scorehuman))

#affichage du score final
if (scorehuman > scorecomp):
    print("Victoire de l'etre humain !")
elif (scorehuman < scorecomp):
    print("Victoire de l'ordinateur !")
else:
    print("Egalite")






