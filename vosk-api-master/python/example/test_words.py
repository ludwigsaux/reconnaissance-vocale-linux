#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import json
import os
import wave
import configparser
import queue

def tests(num): #fonction permettant décrire ce que dit la personne dans un fichier texte
    fichier = open("/home/user/Bureau/git/data.txt", "a") #ouvre en écriture le fichier texte
    fichier.write(str(num)) #écrit dans le fichier texte
    fichier.close() 
    
if not os.path.exists("model"):
    print ("Veuillez télécharger un modéle de langue ici : https://alphacephei.com/vosk/models et décompresser le en 'model' dans le dossier actuel.")
    exit (1)

wf = wave.open("/home/user/Bureau/git/vosk-api-master/python/example/test.wav", "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")

# You can also specify the possible word or phrase list as JSON list, the order doesn't have to be strict
rec = KaldiRecognizer(model, wf.getframerate(), '["oh one two three four five six seven eight nine zero", "[unk]"]')
help_dict = {  #dictionnaire de données permettant de transformer quatre en 4 etc...
                    'un': '1', 
                    'deux': '2', 
                    'trois': '3', 
                    'quatre': '4', 
                    'cinq': '5', 
                    'six': '6', 
                    'sept': '7', 
                    'huit': '8', 
                    'neuf': '9', 
                    'zéro' : '0'
                    } 
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())  #récupere les informations transmise par la fonction de reconnaissance
    else:
        print(rec.PartialResult())

Result=rec.FinalResult()
print (Result)
d = json.loads(Result) #transforme les informations en JSON
#print (d["text"])
test_str=d["text"] #récupération de ce qu'a dit la personne
res = ''.join(help_dict[ele] for ele in test_str.split())#traduit les chiffres en caractéres en numérique
#print("chiffre en lettre : ",res)
if(bool(res)==True):#test si quelque chose a été dis/détecté
    tests(res)
else:
    tests("None")


