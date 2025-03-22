
import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine=pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    if c.lower()=="open google":
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif c.lower()=="open youtube":
        webbrowser.open("https://www.youtube.com")
        speak("Opening Youtube")
    elif c.lower()=="open facebook":
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    elif c.lower()=="open twitter":
        webbrowser.open("https://www.twitter.com")    
        speak("Opening Twitter")
    elif c.lower()=="open instagram":
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")
    elif c.lower()=="open whatsapp":
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening Whatsapp")
    pass
 
# Creating a Recognizer instance

if __name__ == "__main__":
    speak("Hello, welcome to the Jarvis ")
    while True:
    # listen foer the wake word "jarvis"
    #obtain the audio from the microphone
     r=sr.Recognizer()
     
    # recognize speech using Google Speech Recognition
     print("Listening...")
     try:
         with sr.Microphone() as source:
           print("Say something")
         audio=r.listen(source,timeout=2,phrase_time_limit=1)

         word=r.recognize_google(audio)
         if (word.lower()=="jarvis"):
            speak("ya")
         # listen for coomand 
            with sr.Microphone() as source:
                print("Jarvis is listening...")
                audio=r.listen(source)
                command=r.recognize_google(audio)
                
                processCommand(command)
                
     except Exception as e:
         print("Error; {0}".format(e))
    