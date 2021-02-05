import sounddevice as sd
from scipy.io.wavfile import write
import os

# define the name of the directory to be created
path = input("Quel est votre nom ?")
path = path + "-01"
os.chdir("trainingData")
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)


fs = 44100  # Sample rate
seconds = 2  # Duration of recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
os.chdir(path)
write('output.wav', fs, myrecording)  # Save as WAV file 
os.chdir("../../")
fichier = open("trainingDataPath.txt", "w")
fichier.write(path+"/"+"output.wav")
fichier.close()
os.system('python modeltraining.py')







