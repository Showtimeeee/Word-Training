import pyttsx3


# text to speech translation
def text_sound(data):
    sound = pyttsx3.init()
    sound.say(data)
    return sound.runAndWait()