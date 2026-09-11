prenom=str(input("entrez votre prenom:"))
if prenom!="":
    print("prenom valide")
else:
     prenom=str(input("entrez un prenom valide:"))    
nom=str(input("entrez votre nom:"))
if nom!="":
    print("nom valide")
else:
    nom=str(input("entrez un nom valide:"))
age=int(input("entrer votre age:"))
classe=str(input("entrer votre classe:"))
note=float(input("entrer votre note:"))
if note<0 or note>20:
    note=float(input("entrer une note comprise entre 0 et 20: "))
nombres_abscences=int(input("entrer le nombre d'abscences:"))
if note >=10 and nombres_abscences<5:
    print("vous etes admis")
elif note >=8 and note<=9.99 :
    print("vous etes en rattrapage")
elif nombres_abscences>=5 or classe=="":
    print("vous etes exclus de l'evaluation")
elif note <10:
    print("mention:insuffisant")  
elif note >=10 and note<=11.99:      
    print("mention:passable")
elif note >=12 and note<=13.99:
    print("mention:assez bien")
elif note >=14 and note<=15.99:
    print("mention:bien")
elif note >=16 and note<=20:
    print("mention:tres bien") 
