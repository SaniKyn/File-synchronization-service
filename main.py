import configparser
import os


def main():
    confing = configparser.ConfigParser()
    confing.read('confing.ini')
    local_folder = confing['SETTINGS']['local_folder']
    cloud_folder = confing['SETTINGS']['cloud_folder']
    token = os.getenv('ACCESS_TOKEN')

    if not token:
        print("Access token not found. Please set the ACCESS_TOKEN environment variable.")
        return 


if __name__ == '__main__':
    main()
