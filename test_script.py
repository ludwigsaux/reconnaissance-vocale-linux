def testSaisie(source): #lors de l'appelle de la fonction test on souhaite recherché les données dans une source précise
    from test import bidule
    if(source!="sourceTest1"): #test si la source entré correpond a une source connu
        source="txt"           #par défaut la source sera un fichier texte
    print("1 - saux") #User1
    print("2 - janicot") #User2
    print("3 - jean") #User3
    valeur=input("Entrer valeur :") 
    if (valeur=="1"):bidule("saux",source,"stdout") 
    if (valeur=="2"):bidule("janicot",source,"stdout")
    if (valeur=="3"):bidule("jean",source,"stdout")
