def testSaisie(source): #lors de l'appelle de la fonction test on souhaite recherché les données dans une source précise
#commande pour tester : python3 -c 'import test_script; print (test_script.testSaisie("txt"))'
    from authRasp import auth
    if(source!="sourceTest1"): #test si la source entré correpond a une source connu
        source="txt"           #par défaut la source sera un fichier texte
    print("1 - saux") #User1
    print("2 - janicot") #User2
    print("3 - jean") #User3
    valeur=input("Entrer valeur :") 
    periph=input("Entrer la sortie souhaité (stdout / autre) : ")#stdout / authent.log
    if (valeur=="1"):auth("Saux",source,periph) 
    if (valeur=="2"):auth("Janicot",source,periph)
    if (valeur=="3"):auth("Jean",source,periph)
