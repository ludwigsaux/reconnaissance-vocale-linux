def clavier(code, username, filetype):
    code=code[:4]#on prend les 4 premiers caractere du code car le retour chariot est compris comme un caractere
    if(type(code)==str):#on verifie le type du code
        if(len(code)<4 or len(code)>4):#Test la longueur du code = Warning!
            print("code invalide")
        else:
            if (filetype=="txt"):
                with open("/home/user/Bureau/git/code.txt") as f:#Ouvre le fichier texte contenant les identifiants
                    mylist = f.read().splitlines()#Divise le fichier texte en ligne
                    for val in mylist:#Explore chaque ligne 
                        if (val.split(";")[1]==code and val.split(";")[0]==username ):#Test chaque ligne
                            return True #retourne True pour a la fonction auth
                    return False #retourne False pour a la fonction auth

