import sounddevice as sd
from scipy.io.wavfile import write
import os

	#Demande le nom de la personne a enregistré
path = input("Quel est votre nom ?")
	#Ajoute -01 au nom afin de fonctionner avec le modeltraining
path = path + "-01"
	#Ouverture dossier trainingData
os.chdir("trainingData")


try:
    os.mkdir(path)
except OSError:
    print ("Création du dossier évoucé " % path)
else:
    print ("Création du dossier réussi " % path)

	#Fréquence du fichier audio en Hz
fs = 44100
	#Durée enregistrement en seconde
seconds = 2
	#Enregistre
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
	#Attend que l'enregistrement soit fini
sd.wait()  
	#Place l'enregistrement dans le dossier de la personne a enregistré
os.chdir(path)
	#Fichier .wav
write('output.wav', fs, myrecording) 
os.chdir("../../")
	#écrit l'emplacement du l'enregistrement
fichier = open("trainingDataPath.txt", "w")
fichier.write(path+"/"+"output.wav")
fichier.close()
	#analyse du fichier audio
os.system('python modeltraining.py')







