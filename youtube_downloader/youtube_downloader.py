from os import path
from sys import argv
from pytube import YouTube, exceptions


HOME = path.expanduser('~')
AUDIO_FILE_PATH = path.join(HOME, 'Music')
VIDEO_FILE_PATH = path.join(HOME, 'Videos')


def download(link: str, download_type='video'):
    try:
        yt_object = YouTube(link)
        if download_type == 'video':
            download_video(yt_object)
        else:
            download_audio_only(yt_object)
        print(f'{yt_object.title} downloaded succesfully.')

    except exceptions.VideoUnavailable as unavailable:
        print(f'ERROR: Video not found\n\tError message: {unavailable}')
    except exceptions.RegexMatchError as invalid_pattern:
        print(
            f'ERROR: Invalid URL pattern.\n\tError message: {invalid_pattern}')
    except Exception as err:
        print(f'Ha ocurrido un error inesperado\n\tError message {err}')


def download_video(yt_object):
    print('Downloading video...')
    filename = f'{yt_object.title}.mp4'.replace(" ", "_")
    yt_object.streams.get_highest_resolution().download(
        output_path=VIDEO_FILE_PATH, filename=filename)


def download_audio_only(yt_object):
    print('Downloading audio...')
    filename = f'{yt_object.title}.mp3'.replace(" ", "_")
    yt_object.streams.get_audio_only().download(
        output_path=AUDIO_FILE_PATH, filename=filename,)


def selection():
    selected = int(input('Ingrese un numero: '))
    while (selected != 1) and (selected != 2):
        selected = int(input('Presione\n1)Audio\n2)Video\n'))
    return selected


def main():
    try:
        if len(argv) == 3:
            link = argv[1]
            download_type = int(argv[2])
        elif len(argv) == 2:
            link = argv[1]
            download_type = selection()

        else:
            link = input('Ingrese el link del video a descargar: ')
            download_type = selection()

        download_types = {
            1: 'audio',
            2: 'video',
        }

        download(link, download_types[download_type])

    except KeyError:
        print('Ha selectionado una opcion invalida...')


if __name__ == '__main__':
    main()
