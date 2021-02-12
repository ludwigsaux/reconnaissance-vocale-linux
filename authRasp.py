def auth(username,source,periph):
    #import
    import configparser #ouverture fichier ini
    import importlib #appel de fonction avec des caractéres spéciaux
    import datetime #date temps réel
    import sys
    import time
    import authServer
    import Clavier
    import queue
    import os
    from playsound import playsound
    
    #ouverture fichier log
    config = configparser.ConfigParser()
    iniFile=config.read('authent.ini')
    print("Fichier .ini chargé : ", iniFile)  #affiche le fichier .ini chargé (utile log)
    log = config['Log']
    
    if(periph!="stdout"):#stdout = sortie console si autre alors on écrit dans le fichier log
        orig_stdout = sys.stdout
        f = open(str(log['log']), 'w')
        sys.stdout = f
        print("Fichier log : ", str(log['log']))
        
    #date - permet d'afficher la date (utile log)
    date = datetime.datetime.now()
    print("Date : ",date)
        
    #identification vocale
    #enregistre la voix avec testvoix.py    
    print("Vous devez parler afin de vous identifier")
    Path = config['Path']
    playsound(str(Path['authVocale']))#joue le son disant que l'on doit parler
    idVocale = importlib.import_module(str(Path['recMic']))#enregistre pendant 10 secondes (modifiable)
    
    if(authServer.analyseVoix(username)==True):#appelle la fonction d'analyse et vérifie si la personne est la bonne
        print("Vous pouvez passer !") #(utile log)
    else:
        print("Voix non correpondante !") #affiche message erreur (utile log)
    
        q = queue.Queue()
        fichier = open("/home/user/Bureau/git/data.txt", "w")
        fichier.close()
        
        #enregistre la voix de l'utilisateur
        playsound(str(Path['enonceOuCode']))#joue le son disant que l'on doit énoncer et/ou taper le code
        import recMicSaisie #fonction enregistrement de la voix afin que l'utiliseur prononce son code / enregistre pendant 3 secondes (modifiable)
        filesize = os.path.getsize("/home/user/Bureau/git/data.txt")#test si le fichier data est vide si il n'est pas vide ce la signifie q'un mot de passe a été tapé
        if(filesize==0):
            fichier = open("/home/user/Bureau/git/data.txt", "w") #ouvre en écriture le fichier texte
            fichier.write("None"+ '\n') #écrit dans le fichier texte
            fichier.close()
        playsound(str(Path['analyse']))#joue le son disant que l'on doit énoncer et/ou taper le code
        authServer.analyseMot()#appelle la fonction analysant ce qu'a dit la personne
        
        if(authServer.analyseBD(username)==True):
            print("vous pouvez passer !") #(utile log)
            return True
        else:
            Path = config['Path']
            filin = open(str(Path['data']), 'r')#ouvre le fichier temporaire avec les données 
            lignes = filin.readlines()#divise le fichier en ligne
            if(Clavier.clavier(lignes[0],username,source)):#lignes[0]=code écrit au clavier
                print ("vous pouvez passer")
                return True
            else:
                print("vous ne pouvez pas passer")