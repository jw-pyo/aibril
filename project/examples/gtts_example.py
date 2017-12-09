from gtts import gTTS
from tempfile import TemporaryFile
import io
import os
import pygame

def say(text='Hello'):

    tts = gTTS(text=text, lang='ko')
    pygame.mixer.init()
    pygame.init()
    with io.BytesIO() as f:
        tts.write_to_fp(f)
        f.seek(0)
        pygame.mixer.music.load(f)
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        pygame.event.set_allowed(pygame.USEREVENT)
        pygame.mixer.music.play()
        pygame.event.wait() # prevent asynchronous end

def save_voice(text='Hello', filename="default.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

if __name__=="__main__":
    say("과제 존나 하기 싫다.")
