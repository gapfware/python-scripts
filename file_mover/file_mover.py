import os
import shutil


def main():

    path = os.path.expanduser('~')
    downloads_folder = f"{path}/Downloads"

    extentions = {
        'audio': ['.mp3', '.aac', '.wav', '.flac', '.alac', '.dsd'],
        'image': ['.jpg', '.png', '.jpeg', '.gif', '.raw'],
        'text': ['.pdf', '.txt', '.doc', '.docx', '.ppt', '.pptx'],
        'video': ['.mp4', '.mpeg', '.mov']
    }

    for filename in os.listdir(downloads_folder):
        file_extention = os.path.splitext(f"{downloads_folder}" + filename)[1].lower()

        if file_extention in extentions['text']:
            shutil.move(filename, f"{path}/Documents/")

        if file_extention in extentions['image']:
            shutil.move(filename, f"{path}/Pictures/")

        if file_extention in extentions['audio']:
            shutil.move(filename, f"{path}/Music/")

        if file_extention in extentions['video']:
            shutil.move(filename, f"{path}/Videos/")

        if file_extention in [".deb", ".exe"]:
            if not os.path.exists(f"{downloads_folder}/softwarePackages"):
                os.mkdir(f"{downloads_folder}/softwarePackages")
            shutil.move(filename, f"{path}/Downloads/softwarePackages/")


if __name__ == '__main__':
    main()
