import pyttsx3


# text to speech translation
def text_sound(data):
    sound = pyttsx3.init()
    sound.setProperty('rate', -100)
    sound.setProperty('voice', 'ru')
    sound.setProperty('volume', 5.0)
    sound.say(data)
    return sound.runAndWait()