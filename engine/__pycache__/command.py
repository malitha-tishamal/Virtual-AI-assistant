import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init('sapi5')  
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 174) 
    print(voices) 
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()

    try:
        # Debugging: List available microphones
        print("Available microphones:")
        print("Available microphones:")
        print("0: Microphone (Realtek Audio)")
        print("1: Microphone (USB Audio Device)")

        # Use the correct microphone index (replace 0 with your microphone's index)
        with sr.Microphone(device_index=0) as source:
            print('listening......')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)

            try:
                audio = r.listen(source, timeout=10, phrase_time_limit=6)
                print('recognizing...')
                query = r.recognize_google(audio, language='en-in')
                print(f"user said: {query}")
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

text = takecommand()
speak("hello,how can i help you")