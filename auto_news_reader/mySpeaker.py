#import the plataform module to identify your OS
import plataform

#if you are using Windows, use pyttsx3 for text to speech
if plataform.system() =="Windows":
    import pyttsx3

    try:
        engine = pyttsx3.init()
    except ImportError:
        pass
    except RuntimeError:
        pass
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.2)

    def print_say(txt):
        print(txt)
        engine.say(txt)
        engine.runAndWait()
#If you are using Mac or Linux, use gtts for text to speech
elif plataform.system() == "Darwin" or plataform.system() == "Linux":
    import os

    def print_say(texts):
        print(texts)
        texts = texts.replace('"', '')
        texts = texts.replace('"', '')
        os.system(f'gtts-cli --noncheck "{texts}" | mpg123 -q -')
        #End of File