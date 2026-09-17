eleves=[]
while True :
 print("=====GESTION DE LA CLASSE=====")
 print("1. ajouter un nouveau élève")
 print("2. Afficher tous les élèves")
 print("3. Afficher les élèves admis")
 print("4. Afficher les élèves non admis")
 print("5. Rechercher un élève")
 print("6. Afficher les statistiques")
 print("7. Supprimer un élève")
 print("8. Quitter")

 OPTION=str(input("veuillez choisir une option"))
 if OPTION=="1":
    nbre_élèves=int(input("quel est le nombre d'eleve a enregistrer"))
    while(nbre_élèves<1 or nbre_élèves>30):
        nbre_élèves=int(input("quel est le nombre d'eleve a enregistrer"))
      
    for i in range(nbre_élèves):
     prenom=str(input("veuillez entrer le prenom de l'élève:"))
     while prenom=="":
        prenom=str(input("veuillez entrer un prenom valide:"))
    
     nom=str(input("veuillez entrer le nom de l'élève:"))
     while nom=="":
        nom=str(input("veuillez entrer un nom valide:"))
    
     age=int(input("veuillez entrer l'age de l'élève:"))
     while age<10 or age>30 :
        age=int(input("veuillez entrer un age comprise entre 10 et 30:"))
    
     note=float(input("veuillez entrer la note de l'élève" ))
     while note<0 or note>20:
        note=float(input("veuillez entrer une note comprise entre 0 et 20:"))
     classe = str(input("veuillez entrer la classe de l'élève:"))
    
     nombre_abscence=int(input("veuillez entrer le nombre d'abscences de l'élève:"))
     while nombre_abscence<0:
        nombre_abscence=int(input("veuillez entrer un nombre d'abscences valide:"))
     if nombre_abscence>=5:
        resultat="Exclu"
     elif note>=10 and nombre_abscence<5:
        resultat="Admis"

     elif (note >=8 and note<10) and nombre_abscence<5:
        resultat="Rattrapage"
        
     else:
        resultat="Non_admis"
        
     dict_eleve={
        "prenom":prenom, 
        "nom":nom, 
        "age":age, 
        "classe":classe,
        "note":note, 
        "absences":nombre_abscence, 
        "resultat":resultat
        }
     eleves.append(dict_eleve)
    
     print("nom complet:",prenom+" "+nom)
     print("note:",note)
     print("nombre d'absences:",nombre_abscence)
     print("resultat:",resultat)
     
 elif OPTION=="2":
    if len(eleves)==0:
     print("Aucun élève enregistré.")
    else:
        for i, eleve in enumerate(eleves):
            print("i+1", eleve["prenom"], eleve["nom"])
            print("   note:", eleve["note"])
            print("   absences:", eleve["absences"])
            print("   resultat:", eleve["resultat"])
 elif OPTION=="3":
    for i in eleves :
       if i["resultat"]=="Admis":
          print(i["prenom"]+" "+i["nom"])
 elif OPTION=="4":
    for i in eleves :
       if i["resultat"]=="Non_admis":
          print(i["prenom"]+" "+i["nom"])
 elif OPTION=="5":
    recherche=str(input("entrer le prenom de l'eleve  que tu veux rechercher"))
    trouve = False
    for i in eleves:
        if recherche.lower() == i["prenom"].lower():
            print(i["prenom"], i["nom"])
            print("age:", i["age"])
            print("classe:", i["classe"])
            print("note:", i["note"])
            print("absences:", i["absences"])
            print("resultat:", i["resultat"])
            trouve = True
    if not trouve:
        print("Aucun élève trouvé.")
 elif OPTION=="6":
      if len(eleves)==0:
        print("aucun eleve enregistre")
      else:
        notes = []
        nombre_admis = 0
        nombre_rattrapage = 0
        nombre_non_admis = 0
        nombre_exclus = 0
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
        print("nombre total d'élèves:", len(eleves))
        print("nombre d'admis:", nombre_admis)
        print("nombre_d'eleves au rattrapage:",nombre_rattrapage )
        print("nombre total d'eleves non admis :",nombre_non_admis)
        print("nombre d'eleves exclus:",nombre_exclus)
        print("moyenne générale:", round(sum(notes) / len(eleves), 2))
        print("meilleure note:", max(notes))
        print("note la plus faible:", min(notes))
 elif OPTION=="7":
    supprimer=str(input("entrer le nom de l'eleve que vous voulez supprimer"))
    trouver=False
    for i in eleves :
       if supprimer.lower()==i["prenom"].lower():
          eleves.remove(i)
          trouver=True
          break
    if not trouver:
       print("l'eleve que vous voullez supprimer n'existe pas")
 elif OPTION=="8":
    print("fin de programme")   
    break
 else:
    print("entrer une option valide")
    
  
     
    
         
    

   



