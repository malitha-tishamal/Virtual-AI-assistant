try:
    from _datetime import * # type: ignore
    from _datetime import __doc__ # type: ignore
except ImportError:
    from _pydatetime import *
    from _pydatetime import __doc__

__all__ = ("date", "datetime", "time", "timedelta", "timezone", "tzinfo",
           "MINYEAR", "MAXYEAR", "UTC")

import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime

def talk(command):
    """Speak the given command using text-to-speech."""
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
        engine.say("Playing " + command)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in talk(): {e}")

def takeCommand():
    """Listen for a voice command and play the requested song on YouTube."""
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)  # Adjust for background noise
            voice = listener.listen(source)
            try:
                command = listener.recognize_google(voice).lower()  # Convert to lowercase for consistency
                print(f"Recognized command: {command}")  # Debugging: Print the recognized command
                if 'play' in command:
                    song = command.replace('play', '').strip()
                    if song:  # Ensure a song name is provided
                        print(f"Playing song: {song}")
                        talk(song)
                        pywhatkit.playonyt(song)
                    else:
                        print("No song name detected after 'play'.")
                        talk("Please specify a song name to play.")
                else:
                    print("No valid command detected. Command did not contain 'play'.")
                    talk("I did not detect a valid command. Please say 'play' followed by the song name.")
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
                talk("Sorry, I could not understand the audio. Please try again.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        talk("There was an issue with the speech recognition service.")
    except Exception as e:
        print(f"Error in takeCommand(): {e}")
        talk("An error occurred while processing your command.")

if __name__ == "__main__":
    print(datetime.now())
    takeCommand()