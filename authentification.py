def auth(username,source,periph):
    #python3 -c 'import test; print (test.testScript("saux"))'	

    #ouverture fichier log
    import configparser
    import sys
    config = configparser.ConfigParser()
    iniFile=config.read('authent.ini')
    print(iniFile)
    log = config['Log']
    if(periph!="stdout"):
        orig_stdout = sys.stdout
        f = open(str(log['log']), 'w')
        sys.stdout = f
        print("Fichier log : ", str(log['log']))
    
    
    #date
    import datetime
    date = datetime.datetime.now()
    print("Date : ",date)
    
    #identification vocale
    import importlib
    import sys
    import time
    print(sys.version_info[0])
    Path = config['Path']
    print(str(Path['recMic']))
    idVocale = importlib.import_module(str(Path['recMic']))

    import os
    os.chdir("idSpeaker")
    os.system('python test.py')
    filin = open(str(Path['data']), 'r')
    lignes = filin.readlines()
    print(lignes[0])
    if(lignes[0]!=username):
        print("ok !!")
        os.chdir("../")
        #import
        import Clavier
        Path = config['Path']
        print(str(Path['micro']))
        vosk_api = importlib.import_module(str(Path['micro']))#appel le fichier permettant d'écouter l'utilisateur
        
        
        
        #appel des fonctions
        Path = config['Path']
        filin = open(str(Path['data']), 'r') #ouvre le fichier contenant ce qu'a dit l'utilisateur
        lignes = filin.readlines()
        with open(str(Path['code'])) as f:#Ouvre le fichier texte
                    mylist = f.read().splitlines() #divise le fichier en ligne
    
        valide=0
        for val in mylist:#Explore chaque ligne 
             if (val.split(";")[1]==lignes[0] and val.split(";")[0]==username ):#Test chaque ligne
                 print("mot de passe bd : ",val.split(";")[1])
                 print("mot de passe prononcé : ",lignes[0])
                 print("username bd : ",val.split(";")[0])
                 print("username : ",username)
                 print("vous pouvez passer !")
                 valide=1
                 break
        if(valide==0): #le code saisie vocalement n'a pas été reconnu alors on entre le code au clavier
                 code = input("code ?")
                 print("code écrit : ",code)
                 test=Clavier.clavier(code,username,source)
                 if(test==1):
                     valide=1
        if(periph!="stdout"):
            sys.stdout = orig_stdout
            f.close()
