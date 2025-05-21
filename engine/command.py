import pyttsx3
import speech_recognition as sr
import eel 
import time

def speak(text):
    engine = pyttsx3.init('sapi5')  
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 174) 
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()



def takecommand():
    r = sr.Recognizer()

    try:
        
        print("Available microphones:")
        print("Available microphones:")
        print("0: Microphone (Realtek Audio)")
        print("1: Microphone (USB Audio Device)")

        e
        with sr.Microphone(device_index=0) as source:
            print('listening......')
            eel.DisplayMessage('listening......')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)

            try:
                audio = r.listen(source, timeout=10, phrase_time_limit=6)
                print('recognizing...')
                eel.DisplayMessage('recognizing...')
                query = r.recognize_google(audio, language='en-in')
                print(f"user said: {query}")
                eel.DisplayMessage(query)
                time.sleep(2)
             

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
                return " "
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return " "
           
            
    except Exception as e:
        print(f"Microphone error: {e}")
        return " "

    return query.lower()
@eel.expose
def allCommands():

    query = takecommand()
    print(query)

    if "open" in query:
        print(" i run")
        from engine.features import openCommand
        openCommand(query)

    elif "on youtube":
        from engine.features import playYoutube
        playYoutube(query)
    
    else:
        print("not run")

    eel.ShowHood()
