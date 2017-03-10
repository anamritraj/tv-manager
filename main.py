"""
    TODO:
    - Manage TV files: Rename, create folders according to name, season, episode etc.
    - Keep track of what has been watched.
    - Keep track of what to watch next.
    - Keep track of which episode airs next and remind to watch it.
    - Get the latest episode from the internet, automatically.
    - Notifications on both phone and PC using Twilio and native notifications API.
"""
from glob import glob
import pprint
import os

EXTENSIONS = [".mp4", ".mkv"]

# PATH = "C:/Users/aaa/Desktop/TODO"
PATH = "D:/TV"


def get_tv_files(PATH):
    """
    Return all the files in a directory, recurcively.
    :param PATH: Path to a dirty folder containing unorganized files.
    :return: List of files in the folder.
    """
    files = []
    for folderName, subfolders, filenames in os.walk(PATH):
        print("Scanning " + folderName)
        for file in filenames:
            for ext in EXTENSIONS:
                if file.endswith(ext):
                    files.append(file)
    return files


def main():
    files = get_tv_files(PATH)
    pprint.pprint(files)

if __name__ == '__main__':
    main()
