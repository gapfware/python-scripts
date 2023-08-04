from sys import argv
from os import remove
from pygame import mixer, time
from gtts import gTTS


def main():

    if len(argv) == 2:
        text = argv[1]
    else:
        text = input("Ingrese el texto: ")

    fileaudio = 'output.mp3'
    tts = gTTS(text, lang='es')
    tts.save(fileaudio)
    mixer.init()
    mixer.music.load(fileaudio)
    mixer.music.play()
    while mixer.music.get_busy():
        time.wait(100)
    remove(fileaudio)


if __name__ == '__main__':
    main()
