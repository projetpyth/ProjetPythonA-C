import random

import sqlite3 as sq

conn = sq.connect("lapatoch.db")
curseur = conn.cursor()


print("Bienvenue dans ce jeu de gestion de pâtisserie !")

print("Votre but est de prendre en charge une entreprise en concurrence avec d'autres entreprises. Le jeu est basé sur"
       " un système de tours de rôle, où vous allez devoir prendre des décisions pour gérer son entreprise à chaque"
       " tour. Les aspects financiers de la gestion d'une entreprise sont inclus et il y aura aussi des contraintes "
       "ainsi que des opportunités. ")

print("Créé par Anna et Corentin en Mars 2023, pour l'année 2022-2023")

print("Mais avant de commencer, assurez vous d'avoir bien compris les règles du jeu:"
      "-Dans ce jeu un tour équivaut à deux semaines dans la réalité."
      "-Le premier tour est un cadeau, il ne se passera rien, c'est pour vous aider à bien lancer votre entreprise"
      "-A partir du deuxième et jusqu'au onzième vous pourrez être amené à avoir quelques problèmes dans votre"
      "entreprise et c'est à vous de les gérer au mieux!!"
      "-Vous aurez une trésorerie au début du premier tour, elle vous permettra de bien commencer la partie, à vous "
      "de la dépenser à bon escient!"
      "C'est parti!")
nom = input("Veuillez choisir un nom pour votre entreprise:")
id = input("Veuillez choisir un nom de Joueur:")



print("Début du tour: 1")
print("Votre score est de 0.")

score =0
tour = 1
satisfactionClient = 4
chiffresdaffaires = 0

for loop in range (1,11):
    def evenement():
        if tour == 1:
            print("Pas d'évènement ce tour-ci, attention au prochain tour...!")
        else:
            print("Attention ça va se corser !! ")
    print(" Un évènement va apparaitre pour rendre la tâche un peu plus complexe.")

    evenements = {
        "Inflation": 0.05,
        "Demande": 0.05,
        "Hors Service": 0.025,
        "Pandémie": 0.025,
        "Grève": 0.025,
        "Innondation": 0.015,
        "Concurrence": 0.05,
        "Nouveaux concu": 0.05,
        "Opportunités de prêts": 0.025,
        "Aides": 0.01,
        "Dons": 0.01,
        "Bénévolat": 0.005,
        "Fournisseurs": 0.01,
        "Problèmes fournisseurs": 0.15
    }


    def get_evenement():
        choix = random.uniform(0, 1)
        probacumul = 0
        for evenement, proba in evenements.items():
            probacumul += proba
            if choix < probacumul:
                return evenement


    print("Appuyez sur 1 si vous voulez acheter des matières premières")
    print("Appuyer sur 2 si vous voulez voir vos matières premières disponibles")
    print("Appuyez sur 3 pour gérer vos salariés (nombre et salaires")
    print("Appuyez sur 4 si vous voulez acheter un four")
    print("Appuyer sur 5 si vous voulez faire varier les prix de vos produits")
    print("Appuyer sur 6 pour ajouter et/ou enlever un nouveau produit")
    print("Appuyer sur 7 pour voir vos finances")
    print("Appuyer sur 8 si vous voulez avancer dans le tour")


    choix=input("Entrer votre choix:")
    if choix== 1:
        def matPrem ():
              nomM = int(input("Entrer le nom de la matière:"))
              curseur.execute("SELECT * FROM Ressources WHERE nomM=nomRess")
              for matPrem in curseur.fetchall() :
                  print (nomRess[0], coutsRess [1], qteDispo [2])
                  qteDde = int(input("Combien de quantité voulez-vous?"))
                  if qteDde <= qteDispo[2]:
                      curseur.execute("UPDATE Joueurs SET stockMatPrem = stockMatPrem+"+qteDde)
                      valeur= qteDde * coutsRess
                      curseur.execute("UPDATE Joueurs SET tresoreriEntp = tresoreriEntp-"-valeur)
                      score +=qteDde
                  else:
                      print("Il n'y a pas assez de quantité desponible.")
                      curseur.execute("UPDATE Joueurs SET stockMatPrem = stockMatPrem+"+qteDispo)
                      valeurs= qteDispo * coutsRess
                      curseur.execute("UPDATE Joueurs SET tresoreriEntp=tresorerieEntp-"-valeurs)

    if choix== 2:
       def matPremdispo():
              print("Matières premières disponibles:")
              curseur.execute("SELECT stockMatPrem FROM Joueurs")
       for MatPremDispo in curseur.fetchall():
           print (stockMatPrem[3])

    if choix==3:
       def salarie():
           curseur.execute("SELECT nomRess FROM Ressources WHERE nomRess= workers")
           print ("Choisir 1 pour embaucher un salarié")
           print ("Choisir 2 pour licencier un salarié")
           print ("Chosir 3 pour augmenter le salaire")
           print ("Choisir 4 pour diminuer le salaire")
           s = input("Entrer votre choix:")

           if s== 1:
              nbr=int(input("Combien de salarié voulez-vous")
              curseur.execute("UPDATE Ressources SET qteWorkers = qteWorkers+"+nbr)
              score +=nbr
              print("Vous avez maintenant:" qteWorkers [8] "salarié")
              elif s==2:
               nbr=int(input("Combien de salarié voulez-vous")
              curseur.execute("UPDATE Ressources SET qteWorkers=qteWorkers+"+nbr)
                               print("Vous avez maintenant:"qteWorkers[8]"salarié.")


           salaire = input ("Entrer le montant que vous voulez ajouter ou en enlever:")
           s= int(input("Entrer votre choix:")

           if s==3:
               curseur.execute ("UPDATE Ressources SET coutsRess = coutsRess+"+salaire)
               print("Vos travailleurs ont maintenant un salaire de:"{coutsRess})

           if s==4:
               curseur.execute ("UPDATE Ressources SET coutsRess =coutsRess-"-salaire)
               print("Vos travailleurs ont maintenant un salaire de:" {coutsRess})

    if choix==4:
    def four():
           curseur.execute("SELECT qteEquipement FROM Joueurs")
           qteFour = int(input("Combien de four voulez-vous?"))
           if qteFour <= qteDispo[2]:
               curseur.execute("UPDATE Joueurs SET qteEquipement =qteEquipement +"+qteFour)
               val= qteFour * coutsRess
               curseur.execute("UPDATE Joueurs SET tresoreriEntp =tresoreriEntp-"-val)
               score +=qteFour*2
           else:
               print("Il n'y a pas assez de four disponible.")
               curseur.execute("UPDATE Joueurs SET stockMatPrem = stockMatPrem+"+qteDispo)
               vall= qteDispo * coutsRess
               curseur.execute("UPDATE Joueurs SET tresoreriEntp = tresoreriEntp-"-vall)


    if choix==5:
       def price():
           nProduit = int(input("Entrer la pâtisserie que vous voulez:"))
           curseur.execute("SELECT * FROM Produits WHERE nomProduit = nProduit")
       for nPd in curseur.fetchall() :
                 print (nomProduit [0], prixProduits [2])
                 prixnv = int(input("Mettez votre nouveau prix?"))
                 curseur.execute("UPDATE Produits SET prixProduits=+"+prixnv)
                 score +=1

    if choix==6:
      def produit():
            nomP = int(input("Entrer le nom du produit que vous voulez ajouter:")
            prixP = int(input("Entrer le prix que vous voulez mettre pour ce produit;")
            curseur.execute("INSERT INTO Produits (nomProduit, qteStock, prixProduits) VALUES ("nomP, 0, prixP")")

    if choix==7:
       def finance():
              print("Voici vos finances:")
              curseur.execute("SELECT tresoreriEntp FROM JOUEURS")
       for finance in curseur.fetchall():
              tresoreriEntp = resultat[4]
              print(tresoreriEntp [3])

    if choix==8:
       def produitsdispos():
           print("Voici les produits disponibles:")
           curseur.execute("SELECT nomProduit FROM Produits")
           for produitsdispos in curseur.fetchall():
               print(nomProduit[0])

    for loop in range (random.randrange(1,11)):
    def commande():
        print("La commande du client est:")
        curseur.execute("SELECT * FROM Produits")
        return random.choice(nomProduit[0])
    print("Le client demande:")
    quantitedemande = random.randrange(1, 5)
    print(quantitedemande)
    print("Au prix de:")
    total = quantitedemande * prixproduits[2]
    print(quantitedemande * prixproduits[2])
    curseur.execute("UPDATE Produits SET qteStock = qteStock-"-quantitedemande"WHERE nomProduit"= random.choice)
    chiffresdaffaires+=total
    satisfactionClient += random.uniform(0.2,1.2)
    score+=quantitedemande

    def score():
        print("Voici vos résultats de fin de tour:")
        print("Votre chiffres d'affaire est de:", chiffresdaffaires)
        print("Votre score est de:", score)
        print("La satisfaction client est de:", satisfactionClient)

tour += 1
print("Tour n°:", tour)

print("Nous venons de recevoir vos résultats. Vous pourrez faire mieux la prochaine fois.")
print("Merci d'avoir joué à notre jeu !!"
      "En espérant vous revoir bientôt (ou pas).")
print("Conçu par A-C Development")





