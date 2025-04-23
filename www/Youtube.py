import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser

def talk(command):
    """Speak the given command using text-to-speech."""
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    engine.say(command)
    engine.runAndWait()

def takeCommand():
    """Listen for a voice command and execute the corresponding action."""
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source) 
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()  
            print(f"Command received: {command}")

            if 'play' in command:
                song = command.replace('play', '').strip()
                talk(f"Playing {song} on YouTube")
                pywhatkit.playonyt(song)
            elif 'open youtube' in command:
                talk("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
            elif 'open facebook' in command:
                talk("Opening Facebook")
                webbrowser.open("https://www.facebook.com")
            elif 'open whatsapp' in command:
                talk("Opening WhatsApp")
                webbrowser.open("https://web.whatsapp.com")
            elif 'open google' in command:
                talk("Opening Google")
                webbrowser.open("https://www.google.com")
            elif 'open email' in command:
                talk("Opening Email")
                webbrowser.open("https://mail.google.com")
            else:
                talk("Sorry, I didn't understand that command.")
                print("No valid command detected.")
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio.")
        talk("Sorry, I did not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        talk("There was an issue with the speech recognition service.")
    except Exception as e:
        print(f"Error: {e}")
        talk("An error occurred while processing your command.")

if __name__ == "__main__":
    takeCommand()