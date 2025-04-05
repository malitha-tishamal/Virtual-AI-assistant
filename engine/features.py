from playsound import playsound
import eel

#playing assistant sound

@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\audio\\audio.mp3"
    playsound(music_dir)