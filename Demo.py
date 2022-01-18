from urllib import response
from Google import Create_Service
import pandas as pd

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


def get_storage_info():
    response = service.about().get(fields="*").execute()

    for k, v in response.get("storageQuota").items():
        print('{0}:{1:.2f}MB'.format(k, int(v) / 1024**2))
        print('{0}:{1:.2f}GB'.format(k, int(v) / 1024**3))

    print(response.get("user")['displayName'])


print(get_storage_info())


def get_old_files(date: str):
    """ This function returns files that are not modified after a given data"""

    query = "modifiedTime < '{}'".format(date)
    get_all_files = service.files().list(q=query).execute()
    matched_files = get_all_files.get('files')
    nextPageToken = get_all_files.get('nextPageToken')

    while nextPageToken:
        get_all_files = service.files().list(q=query, pageToken=nextPageToken).execute()
        matched_files.extend(get_all_files.get('files'))
        nextPageToken = get_all_files.get('nextPageToken')

    for file in matched_files:
        print(file)

# print(get_old_files('2017-06-04'))


def delete_files(fileId_list):
    for id in fileId_list:
        service.files().delete(
            fileId=id
        ).execute()


# delete_files([''])
