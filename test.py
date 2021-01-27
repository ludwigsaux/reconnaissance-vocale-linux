def bidule(username,source,periph):
    #python3 -c 'import test; print (test.testScript("saux"))'
    vosk_api = __import__("vosk-api-master.python.example.test_microphone")
    microphone = getattr(vosk_api, "test_microphone")
    microphone.example_func()
    import Clavier
    #test_microphone #appel le fichier permettant d'écouter l'utilisateur
    filin = open("/home/user/Bureau/git/data.txt", "r") #ouvre le fichier contenant ce qu'a dit l'utilisateur
    lignes = filin.readlines()
    with open("/home/user/Bureau/git/code.txt") as f:#Ouvre le fichier texte
                mylist = f.read().splitlines() #divise le fichier en ligne

    valide=0
    for val in mylist:#Explore chaque ligne 
          if (val.split(";")[1]==lignes[0] and val.split(";")[0]==username ):#Test chaque ligne
              print(val.split(";")[1])
              print(lignes[0])
              print(val.split(";")[0])
              print(username)
              print("vous pouvez passer !")
              valide=1
    if(valide==0): #le code saisie vocalement n'a pas été reconnu alors on entre le code au clavier
              code = input("code ?")
              test=Clavier.clavier(code,username,source)
              if(test==1):
                  valide=1
