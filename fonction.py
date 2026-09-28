# Liste qui contient tous les élèves enregistrés
eleves=[]

# Ajoute un ou plusieurs élèves dans la liste
def ajouter_eleve():
   # Demande le nombre d'élèves à enregistrer
   nbre_élèves=int(input("quel est le nombre d'eleve a enregistrer:"))
   # Vérification : le nombre doit être entre 1 et 30
   while(nbre_élèves<1 or nbre_élèves>30):
      nbre_élèves=int(input("quel est le nombre d'eleve a enregistrer :"))
   for i in range(nbre_élèves):
      # À partir du 2e élève, on demande si l'utilisateur veut continuer
      if i > 0:
         continuer = input("Continuer la saisie ? (o/n) : ")
         if continuer != "o":
            break
      # Demande le prénom et verification
      prenom=str(input("prenom:"))
      while prenom=="":
         prenom=str(input("veuillez entrer un prenom valide:"))
      # Demande le nom et verification
      nom=str(input("nom:"))
      while nom=="":
         nom=str(input("veuillez entrer un nom valide:"))
      # Demande l'âge et vérification
      age=int(input("age:"))
      while age<10 or age>30 :
         age=int(input("veuillez entrer un age comprise entre 10 et 30:"))
      # Demande la note et vérification
      note=float(input("note:" ))
      while note<0 or note>20:
         note=float(input("veuillez entrer une note comprise entre 0 et 20:"))
      # Demande la classe
      classe = str(input("classe:"))
      # Demande le nombre d'absences et vérification
      nombre_abscence=int(input("nombre d'abscence:"))
      while nombre_abscence<0:
         nombre_abscence=int(input("veuillez entrer un nombre d'abscences valide:"))
      # Détermination du résultat selon la note et les absences
      if nombre_abscence>=5:
         resultat="Exclu"
      elif note>=10 and nombre_abscence<5:
         resultat="Admis"
      elif (note >=8 and note<10) and nombre_abscence<5:
         resultat="Rattrapage"
      else:
         resultat="Non_admis"
      # Création d'un dictionnaire pour stocker les infos de l'élève
      dict_eleve={
         "prenom":prenom,
         "nom":nom,
         "age":age,
         "classe":classe,
         "note":note,
         "absences":nombre_abscence,
         "resultat":resultat
         }
      # Ajout de l'élève dans la liste
      eleves.append(dict_eleve)
      # Affichage des infos de l'élève ajouté
      print("eleve enregistrer:",dict_eleve)

# Affiche les élèves; si un filtre est donné, on ne montre que ceux du bon résultat
def afficher_eleves(eleves,filtre=None):
   if len(eleves)==0:
      print("Aucun élève enregistré.")
      return
   trouve = False
   for i, eleve in enumerate(eleves):
      if filtre is None or eleve["resultat"] == filtre:
         print("eleve numero",i+1, ":", eleve["prenom"], eleve["nom"])
         print("   note:", eleve["note"])
         print("   absences:", eleve["absences"])
         print("   resultat:", eleve["resultat"])
         trouve = True

   if not trouve:
      print("Aucun élève ne correspond à ce critère")

# Recherche un élève par son prénom et affiche ses informations
def recherche_eleves(eleves,prenom):
   if len(eleves)==0:
      print("Aucun élève enregistré")
      return
   trouve=False
   for i in eleves:
      if i["prenom"]==prenom:
         print(i["prenom"], i["nom"])
         print("age:", i["age"])
         print("classe:", i["classe"])
         print("note:", i["note"])
         print("absences:", i["absences"])
         print("resultat:", i["resultat"])
         trouve=True

   if not trouve:
      print("Aucun élève trouvé.")

# Calcule les statistiques globales de la classe
def afficher_statistique(eleves):
   if len(eleves)==0:
      print("aucun eleve enregistre")
      return
   notes = []
   nombre_admis = 0
   nombre_rattrapage = 0
   nombre_non_admis = 0
   nombre_exclus = 0
   # Parcours de tous les élèves pour calculer les statistiques
   for i in eleves:
      notes.append(i["note"])
      if i["resultat"] == "Admis":
         nombre_admis += 1
      elif i["resultat"] == "Rattrapage":
         nombre_rattrapage+=1
      elif i["resultat"] == "Non_admis":
         nombre_non_admis+=1
      elif i["resultat"] == "Exclu":
         nombre_exclus+=1
   # Affichage des résultats statistiques
   print("nombre total d'élèves:", len(eleves))
   print("nombre d'admis:", nombre_admis)
   print("nombre d'eleves au rattrapage:",nombre_rattrapage )
   print("nombre d'eleves non admis:",nombre_non_admis)
   print("nombre d'eleves exclus:",nombre_exclus)
   print("moyenne générale:", round(sum(notes) / len(eleves), 2))
   print("meilleure note:", max(notes))
   print("note la plus faible:", min(notes))

# Supprime un élève à partir de son prénom
def supprimer_eleves(eleves,prenom):
   if len(eleves)==0:
      print("aucun eleve enregistre")
      return
   trouver=False
   # Recherche l'élève à supprimer
   for i in eleves :
      if prenom==i["prenom"]:
         eleves.remove(i)
         trouver=True
         break
   # Message si l'élève n'existe pas
   if not trouver:
      print("l'eleve que vous voulez supprimer n'existe pas")

# Menu principal du programme
while True:
   print()
   print("=====GESTION DE LA CLASSE=====")
   print("1. ajouter un nouveau élève")
   print("2. Afficher tous les élèves")
   print("3. Afficher les élèves admis")
   print("4. Afficher les élèves non admis")
   print("5. Rechercher un élève")
   print("6. Afficher les statistiques")
   print("7. Supprimer un élève")
   print("8. Quitter")
   # ici on demande à l'utilisateur de choisir une option
   OPTION = input("veuillez choisir une option:")
   # appel des fonctions selon le choix
   if OPTION == "1":
      ajouter_eleve()

   elif OPTION == "2":
      afficher_eleves(eleves)

   elif OPTION == "3":
      afficher_eleves(eleves, "Admis")

   elif OPTION == "4":
      afficher_eleves(eleves, "Non_admis")

   elif OPTION == "5":
      prenom_cherche = input("entrer le prenom de l'eleve que tu veux rechercher:")
      recherche_eleves(eleves, prenom_cherche)

   elif OPTION == "6":
      afficher_statistique(eleves)

   elif OPTION == "7":
      prenom_a_supprimer = input("entrer le prenom de l'eleve que vous voulez supprimer:")
      supprimer_eleves(eleves, prenom_a_supprimer)

   elif OPTION == "8":
      print("fin de programme")
      break

   else:
      print("entrer une option valide")