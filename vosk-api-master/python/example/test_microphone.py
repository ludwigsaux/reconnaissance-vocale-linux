#!/usr/bin/env python3

import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import json
from playsound import playsound
import configparser

config = configparser.ConfigParser()
iniFile=config.read('authent.ini')
Path = config['Path']


q = queue.Queue()
fichier = open(str(Path['data']), "w")
fichier.close()
def tests(num): #fonction permettant décrire ce que dit la personne dans un fichier texte
    fichier = open(str(Path['data']), "a") #ouvre en écriture le fichier texte
    fichier.write(str(num)) #écrit dans le fichier texte
    fichier.close() 

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata)

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    '-f', '--filename', type=str, metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-m', '--model', type=str, metavar='MODEL_PATH',
    help='Path to the model')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
args = parser.parse_args(remaining)

try:
    if args.model is None:
        args.model = "model"
    if not os.path.exists(args.model):
        print ("Please download a model for your language from https://alphacephei.com/vosk/models")
        print ("and unpack as 'model' in the current folder.")
        parser.exit(0)
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, 'input')
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info['default_samplerate'])

    model = vosk.Model(args.model)

    if args.filename:
        dump_fn = open(args.filename, "wb")
    else:
        dump_fn = None

    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device, dtype='int16',
                            channels=1, callback=callback):
            print('#' * 80)
            print('Press Ctrl+C to stop the recording')
            print('#' * 80)

            rec = vosk.KaldiRecognizer(model,args.samplerate)
            
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
            playsound(str(Path['parler']))#joue le son disant que l'on doit parler
            digit=0
            while True:

             data = q.get()
             if rec.AcceptWaveform(data): #verifie si du son est détecter
                   
                   
                   test=rec.Result()  #récupere les informations transmise par la fonction de reconnaissance
                   print (test)
                   d = json.loads(test) #transforme les informations en JSON
                   
                   print (d["text"])
                   test_str=d["text"] #récupération de ce qu'a dit la personne
                   
                   res = ''.join(help_dict[ele] for ele in test_str.split())#traduit les chiffres en caractéres en numérique
                   print("chiffre en lettre : ",res)
                   
                   if(len(res)==1 and digit!=4):#Test la longueur du code
                          tests(res)
                          digit=digit+1#compteur permettant de voir combien de chiffre ont été dis
                          playsound(str(Path['chiffreSaisie']))#joue le son correpondant a l'entrée d'un chiffre
                          print("chiffre numéro : ",digit)
                   if(digit==4) :      
                          playsound(str(Path['codeSaisie']))#joue le son signifiant que le code est saisie
                          break#mets fin a la boucle une fois que le code a été saisie
                   
             else:
                    print(rec.PartialResult())
             if dump_fn is not None:
                    dump_fn.write(data)

except KeyboardInterrupt:
    print('\nFin')
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ':' + str(e))


