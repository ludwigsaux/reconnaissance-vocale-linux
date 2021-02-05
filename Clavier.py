def clavier(code, username, filetype):
    if(len(code)<4 or len(code)>4):#Test la longueur du code = Warning!
        print("code invalide")
    else:
        if (filetype=="txt"):
            with open("/home/user/Bureau/git/code.txt") as f:#Ouvre le fichier texte contenant les identifiants
                mylist = f.read().splitlines()#Divise le fichier texte en ligne
        valide=0
        for val in mylist:#Explore chaque ligne 
            if (val.split(";")[1]==code and val.split(";")[0]==username ):#Test chaque ligne
                print ("vous pouvez passer")
                return 1 #retourne 1 pour a la fonction auth
        if (valide==0):
            print("vous ne pouvez pas passer")
            return 0 #retourne 0 pour a la fonction auth

