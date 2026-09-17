# On crée une liste vide qui va contenir tous les élèves enregistrés
eleves=[]
# Boucle infinie : le menu se réaffiche tant que l'utilisateur ne choisit pas de quitter
while True :
 # Affichage du menu principal
 print("=====GESTION DE LA CLASSE=====")
 print("1. ajouter un nouveau élève")
 print("2. Afficher tous les élèves")
 print("3. Afficher les élèves admis")
 print("4. Afficher les élèves non admis")
 print("5. Rechercher un élève")
 print("6. Afficher les statistiques")
 print("7. Supprimer un élève")
 print("8. Quitter")
# Demande à l'utilisateur de choisir une option
 OPTION=int(input("veuillez choisir une option"))
 # Demande à l'utilisateur de choisir une option
 match OPTION:
   case 1:
    # Demande le nombre d'élèves à enregistrer
    nbre_élèves=int(input("quel est le nombre d'eleve a enregistrer"))
    # Vérification : le nombre doit être entre 1 et 30
    while(nbre_élèves<1 or nbre_élèves>30):
      nbre_élèves=int(input("quel est le nombre d'eleve a enregistrer"))
    # Boucle pour enregistrer plusieurs élèves
    for i in range(nbre_élèves):
     # À partir du 2e élève, on demande si l'utilisateur veut continuer
     if i > 0:
            continuer = input("Continuer la saisie ? (o/n) : ").strip().lower()
            if continuer != "o":
                break
     # Demande le prénom et verification
     prenom=str(input("veuillez entrer le prenom de l'élève:"))
     while prenom=="":
        prenom=str(input("veuillez entrer un prenom valide:"))
     # Demande le nom et verification
     nom=str(input("veuillez entrer le nom de l'élève:"))
     while nom=="":
        nom=str(input("veuillez entrer un nom valide:"))
     # Demande l'âge et vérification
     age=int(input("veuillez entrer l'age de l'élève:"))
     while age<10 or age>30 :
        age=int(input("veuillez entrer un age comprise entre 10 et 30:"))
     # Demande la note et vérification
     note=float(input("veuillez entrer la note de l'élève" ))
     while note<0 or note>20:
        note=float(input("veuillez entrer une note comprise entre 0 et 20:"))
     # Demande la classe
     classe = str(input("veuillez entrer la classe de l'élève:"))
     # Demande le nombre d'absences et vérification
     nombre_abscence=int(input("veuillez entrer le nombre d'abscences de l'élève:"))
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
     print(dict_eleve)
   
   case 2:
    # Si la liste est vide, on affiche un message
    if len(eleves)==0:
     print("Aucun élève enregistré.")
    else:
        # On affiche tous les élèves enregistrés
        for i, eleve in enumerate(eleves):
            print("i+1", eleve["prenom"], eleve["nom"])
            print("   note:", eleve["note"])
            print("   absences:", eleve["absences"])
            print("   resultat:", eleve["resultat"])
   case 3:
    # Si la liste est vide, on affiche un message
    if len(eleves)==0:
         print("Aucun élève enregistré.")
    # Affiche uniquement les élèves admis
    for i in eleves :
       if i["resultat"]=="Admis":
          print(i["prenom"]+" "+i["nom"])
   case 4:
    # Affiche uniquement les élèves non admis
    for i in eleves :
       if i["resultat"]=="Non_admis":
          print(i["prenom"]+" "+i["nom"])
   case 5:
    # Recherche un élève par son prénom et initialiser trouve a false
    recherche=str(input("entrer le prenom de l'eleve  que tu veux rechercher"))
    trouve = False
    # Parcours de la liste pour trouver l'élève et d'afficher ces informations
    for i in eleves:
        if recherche.lower() == i["prenom"].lower():
            print(i["prenom"], i["nom"])
            print("age:", i["age"])
            print("classe:", i["classe"])
            print("note:", i["note"])
            print("absences:", i["absences"])
            print("resultat:", i["resultat"])
            trouve = True
    # Si aucun élève n'a été trouvé on lui affiche le message 
    if not trouve:
        print("Aucun élève trouvé.")
   # Affichage des statistiques globales
   case 6:
      if len(eleves)==0:
        print("aucun eleve enregistre")
      else:
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
        print("nombre_d'eleves au rattrapage:",nombre_rattrapage )
        print("nombre total d'eleves non admis :",nombre_non_admis)
        print("nombre d'eleves exclus:",nombre_exclus)
        print("moyenne générale:", round(sum(notes) / len(eleves), 2))
        print("meilleure note:", max(notes))
        print("note la plus faible:", min(notes))
   case 7:
    # Suppression d'un élève selon son prénom 
    supprimer=str(input("entrer le nom de l'eleve que vous voulez supprimer"))
    trouver=False
    # Recherche l'élève à supprimer
    for i in eleves :
       if supprimer.lower()==i["prenom"].lower():
          eleves.remove(i)
          trouver=True
          break
    # Message si l'élève n'existe pas
    if not trouver:
       print("l'eleve que vous voullez supprimer n'existe pas")
   case 8:
    # quitter le programme
    print("fin de programme")
    break   
   case _:
    # Cas par défaut si l'option n'est pas valide
    print("entrer une option valide")
    
  
     
    
         
    

   



