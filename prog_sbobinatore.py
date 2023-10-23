import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import winsound


print("                   |\=.")
print("                   /  6',")
print("           .--.    \  .-'")
print("          /_   \   /  (_()")
print("            )   | / `;--'")
print("           /   / /   (")
print("          (    `'    _")
print("           `-==-'`''''''`")

a = input ("Nome del file da sbobinare: ")


winsound.PlaySound("parte1buona.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )

def registra(a):
    r = sr.Recognizer()                                                     
    audio = sr.AudioFile(a + ".wav")
    with audio as source:
    audio = r.record(source)                  
    result = r.recognize_google(audio,language="it-IT")
    return result


b = input("Vuoi salvare il testo in un file? ")
if b == "sì" or "Sì":
    c = input("Inserisci il titolo del file da creare: ")
    dt = open(c + '.docx', 'w')
    dt.write(result)
    dt.close()
    print("Il file è stato salvato nella cartella corrente.")
    print("Buono studio!")
    
y = input ("Premi invio per uscire.")