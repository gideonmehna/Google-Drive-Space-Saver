from urllib import response
import io
import os
from attr import fields
from googleapiclient.http import MediaIoBaseDownload
from numpy import delete
from Google import Create_Service
import pandas as pd
import json
from random import randint

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


def get_storage_info():
    """
    We are going to return organized text about the drive. 
    """
    drive_info = ""
    response = service.about().get(fields="*").execute()

    for k, v in response.get("storageQuota").items():
        drive_info += ' {0} : {1:.2f}MB '.format(k, int(v) / 1024**2)
        # print('{0}:{1:.2f}MB'.format(k, int(v) / 1024**2))
        # print('{0}:{1:.2f}GB'.format(k, int(v) / 1024**3))
    return drive_info

# print(get_storage_info())


def get_file_size(file_id):
    response = service.files().get(fileId=file_id, fields="size").execute()
    file_size = int(response['size'])

    # print('{0}:{1:.2f}MB'.format("size", file_size / 1024**2))
    return '{0:.2f}MB'.format(file_size / 1024**2)


# print(get_file_size('1Sm6htL0h3YIyDrTLB_4Lc9e5OyU5lPyS'))


def get_old_files(date: str):
    """ This function returns files that are not modified after a given data"""
    # added a file variable
    file = {}

    query = "modifiedTime < '{}'".format(date)
    get_all_files = service.files().list(q=query).execute()

    # matched_files is a list of dictionary
    matched_files = get_all_files.get('files')
    nextPageToken = get_all_files.get('nextPageToken')

    while nextPageToken:
        get_all_files = service.files().list(q=query,
                                             pageToken=nextPageToken).execute()
        matched_files.extend(get_all_files.get('files'))
        nextPageToken = get_all_files.get('nextPageToken')
    # checking if the matched_files has data
    if len(matched_files) == 0:
        return None
    with open("keep_file.json", "r", encoding="utf-8") as f:
        list_of_kept_file = json.load(f)
        # Instead of running through all the files in matched file. We will choose one(or any number) file and check if it is in the list and then choose another if we dont get.
        # for file in matched_files:
        #     if file not in list_of_kept_file:
        #         print(file)
        have_not_got_file = True
        # print(matched_files)
        while have_not_got_file:
            random_file_index = randint(0, len(matched_files)-1)
            # checking if the random file chosen has not already been chosen.
            if matched_files[random_file_index] not in list_of_kept_file:
                file = matched_files[random_file_index]
                have_not_got_file = False
    return file
#

# print(get_old_files('2022-01-21'))


class Buttons():
    def keep_file(file: dict):
        """update keep_file.json by adding the given file_id which the user want to keep """

        with open("keep_file.json", "r+", encoding="utf-8") as f:

            file_data = json.load(f)
            file_data.append(file)

            f.seek(0)

            json.dump(file_data, f, ensure_ascii=False, indent=4)

    def delete_file(file: dict):
        """deletes the file completely and cannot be undone"""
        id = file['id']
        service.files().delete(
            fileId=id
        ).execute()

    def back_up(file: dict):
        """ first downloads the file then deletes the file completely 
            from the drive by calling delete_file function"""

        request = service.files().get_media(fileId=file['id'])

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=request)
        done = False

        while not done:
            status, done = downloader.next_chunk()
            print('Download progress {0}'.format(status.progress() * 100))

        fh.seek(0)

        with open(os.path.join('C:/Users/ugstu/Downloads/Gui', file['name']), 'wb') as f:
            f.write(fh.read())
            f.close()

        Buttons.delete_file(file)


# Buttons.back_up({'kind': 'drive#file', 'id': '1SZKvVCD6H6tcIRGTodrs0MeFRMBIex9X',
#                 'name': 'mat223_reading_3_1-3_2.pdf', 'mimeType': 'application/pdf'})

# Buttons.keep_file({'kind': 'drive#file', 'id': '1BBuk3jIh9LfDYW6brh1LSgxCLoE8zb0O', 'name': 'HKCEE - biology - 2004 - Paper I&II.pdf', 'mimeType': 'application/pdf'})
