#ici j'initialise les compteurs pour le bilan general
Nombre_total_eleves = 0
Nombre_eleve_admis = 0
Nombre_eleve_rattrapage = 0
Nombre_eleve_non_admis = 0
Nombre_eleve_exclus = 0
#je met la boucle while pour que le programme continue tant que l'utilisateur veut enregistrer un autre élève
while True:                 
 print("----- information de l'élève -----")
#je demadnde à l'utilisateur d'entrer les informations de l'élève et je fais des vérifications pour que les informations soient valides
 prenom=str(input("veuillez entrer votre prenom:"))
 while prenom=="":
    prenom=str(input("veuillez entrer un prenom valide:"))

 nom=str(input("veuillez entrer votre nom:"))
 while nom=="":
    nom=str(input("veuillez entrer un nom valide:"))

 age=int(input("veuillez entrer votre age:"))
 while age<10 or age>25 :
    age=int(input("veuillez entrer un age compreis entre 10 et 25:"))
    
 classe = str(input("veuillez entrer votre classe:"))

 note=float(input("veuillez entrer votre note" ))
 while note<0 or note>20:
     note=float(input("veuillez entrer une note comprise entre 0 et 20:"))

 nombre_abscence=int(input("veuillez entrer le nombre d'abscences:"))
 while nombre_abscence<0:
    nombre_abscence=int(input("veuillez entrer un nombre d'abscences valide:"))
# je fais les conditions pour determiner le statut de l'élève et la mention selon les critères donnés et d'incrémenter les compteurs pour le bilan general
 Nombre_total_eleves += 1
 if classe=="" or nombre_abscence>=5:
    statut="exclu"
    Nombre_eleve_exclus += 1
 elif note>=10 and nombre_abscence<5:
    statut="admis"
    Nombre_eleve_admis += 1
 elif note >=8 and note<=10 and nombre_abscence<5:
    statut="rattrapage"
    Nombre_eleve_rattrapage += 1
 else:
    statut="non_admis"
    Nombre_eleve_non_admis += 1

 if note>=0 and note<10:
    mention="insuffisant"
 elif note>=10 and note<12:
    mention="passable"
 elif note>=12 and note<14:
    mention="assez_bien"
 elif note>=14 and note<16:
    mention="bien"
 else: 
    mention="tres_bien"
# je fais l'affichage des informations de l'élève et du bilan general
 print("Eleve:",prenom,nom)
 print("Classe:",classe)
 print("Resultat:",statut)
 print("Mention:",mention)

 if note >=18 and nombre_abscence==0 :
    print("Félicitations du jury" ) 

 # je demande à l'utilisateur s'il veut enregistrer un autre élève et je fais une vérification pour que la réponse soit valide
 reponse=str(input("voulez vous enregistrer un autre eleve? (oui/non)")).lower()
 if reponse!="oui" :
    break
 # je fais l'affichage du bilan general
 print("----- Bilan general -----")
 print("Nombre total d'eleves:", Nombre_total_eleves)
 print("Nombre d'eleves admis:", Nombre_eleve_admis)
 print("Nombre d'eleves au rattrapage:", Nombre_eleve_rattrapage)
 print("Nombre d'eleves non admis:", Nombre_eleve_non_admis)
 print("Nombre d'eleves exclus:", Nombre_eleve_exclus)
 print("fin du programme")
    

