def auth(username,source,periph):
    #python3 -c 'import test; print (test.testScript("saux"))'	

    #import
    import configparser #ouverture fichier ini
    import sys
    import datetime #date temps réel
    import importlib #appel de fonction avec des caractéres spéciaux
    import os #permet de lancer python2 dans python3 (simule terminal)
    import Clavier #fonction code clavier
    
    #ouverture fichier log
    config = configparser.ConfigParser()
    iniFile=config.read('authent.ini')
    print(iniFile)
    log = config['Log']
    if(periph!="stdout"):#stdout = sortie console si autre alors on écrit dans le fichier log
        orig_stdout = sys.stdout
        f = open(str(log['log']), 'w')
        sys.stdout = f
        print("Fichier log : ", str(log['log']))
    
    
    #date - permet d'afficher la date
    date = datetime.datetime.now()
    print("Date : ",date)
    
    #identification vocale
        #enregistre la voix avec testvoix.py    
    Path = config['Path']
    idVocale = importlib.import_module(str(Path['recMic']))

        #test la voix enregistrer avec la base de donnée
    os.chdir("idSpeaker")
    os.system('python test.py')
        #écrit le nom de la personne trouvé
    filin = open(str(Path['data']), 'r')
    lignes = filin.readlines()
    print(lignes[0])
        #test la personne trouvé avec la personne du qrcode
    if(lignes[0]!=username):
        print("ok !!")
        os.chdir("../")
        
            #appel le fichier permettant d'écouter l'utilisateur
        Path = config['Path']
        print(str(Path['micro']))
        vosk_api = importlib.import_module(str(Path['micro']))
        
            #ouvre le fichier contenant ce qu'a dit l'utilisateur
        Path = config['Path']
        filin = open(str(Path['data']), 'r') 
        lignes = filin.readlines()
            #ouvre le fichier texte contenant les identifiants
        with open(str(Path['code'])) as f:
                        #divise le fichier en ligne
                    mylist = f.read().splitlines() 
    
        valide=0
            #Explore chaque ligne 
                #Test chaque ligne
        for val in mylist:
                 #compare le code dit avec le code de la db et compare le nom de la bd avec celui du qrcode
             if (val.split(";")[1]==lignes[0] and val.split(";")[0]==username ):
                 print("mot de passe bd : ",val.split(";")[1])
                 print("mot de passe prononcé : ",lignes[0])
                 print("username bd : ",val.split(";")[0])
                 print("username : ",username)
                 print("vous pouvez passer !")
                     #si le code dit est bon alors valide=1
                 valide=1
                     #on sort de la boucle
                 break
             #le code saisie vocalement n'a pas été reconnu alors on entre le code au clavier
        if(valide==0): 
                 code = input("code ?")
                 print("code écrit : ",code)
                 test=Clavier.clavier(code,username,source)
                 if(test==1):
                     valide=1
        if(periph!="stdout"):
            sys.stdout = orig_stdout
            f.close()
