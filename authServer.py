#import
import os #permet de lancer python2 dans python3 (simule terminal)
import configparser #ouverture fichier ini
import importlib
    
config = configparser.ConfigParser()
iniFile=config.read('authent.ini')
Path = config['Path']
    
def analyseVoix(username):
    #test la voix enregistrer avec la base de donnée
    os.chdir("idSpeaker")
    os.system('python test.py')
    
    #écrit le nom de la personne trouvé dans le fichier data
    filin = open(str(Path['data']), 'r')
    lignes = filin.readlines()
    #print(lignes[0])
    
    #test la personne trouvé avec la personne du qrcode
    if(lignes[0]!=username):
        os.chdir("../")
        return False
    return True
def analyseMot():
        #"/home/user/Bureau/git/vosk-api-master/python/example/test.wav"
        #appel le fichier permettant d'écouter l'utilisateur
        config = configparser.ConfigParser()
        iniFile=config.read('authent.ini')
        Path = config['Path']
        vosk_api = importlib.import_module(str(Path['voix']))

def analyseBD(username):      
        #ouvre le fichier contenant ce qu'a dit l'utilisateur
        Path = config['Path']
        filin = open(str(Path['data']), 'r') 
        lignes = filin.readlines()
        
            #ouvre le fichier texte contenant les identifiants
        with open(str(Path['code'])) as f:
                        #divise le fichier bd en ligne
                    mylist = f.read().splitlines() 
                    
        #Explore chaque ligne 
                #Test chaque ligne
        if(os.path.getsize(str(Path['data']))!=0):
            for val in mylist:
                     #compare le code dit avec le code de la db et compare le nom de la bd avec celui du qrcode
                     if (val.split(";")[1]==lignes[1] and val.split(";")[0]==username ):#lignes[1]=code énoncé
                         
                         print("mot de passe bd : ",val.split(";")[1])
                         
                         print("mot de passe prononcé : ",lignes[1])#(utile log)
                         
                         print("username bd : ",val.split(";")[0])
                         
                         print("username : ",username) #(utile log)
                         return True
                         #on sort de la boucle
                         break
        else:
            return False