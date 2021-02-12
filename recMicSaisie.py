from pynput import keyboard
import time
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

def clavier():#fonction permettant d'écrire le code dans un fichier temporaire
    code = input("code ?")
    fichier = open("/home/user/Bureau/git/data.txt", "w") #ouvre en écriture le fichier texte
    fichier.write(str(code)+ '\n') #écrit dans le fichier texte
    fichier.close() 
    return True
    

break_program = False
def on_press(key):#detecte si une touche est presser puis appelle la fonction clavier
    global break_program
    clavier()
    break_program = True
    return False

#enregister le personne pendant 3 secondes (modifible)
#ajout de 5 secondes d'attente afin que la personne est le temps de taper son code
with keyboard.Listener(on_press=on_press) as listener:
    while break_program == False:
        print ('program running')
        fs = 44100  #Fréquence en Hertz
        seconds = 3  #Durée en seconde
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype=np.int16)
        sd.wait()  #Wait until recording is finished
        write('vosk-api-master/python/example/test.wav', fs, myrecording)  #Save as WAV file 
        time.sleep(5)
        break


