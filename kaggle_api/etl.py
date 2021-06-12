import kaggle 
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

api = KaggleApi()
api.authenticate()


def unzip_file(file_name):
    if ".zip" in file_name:
        with zipfile.ZipFile(file_name, "r") as f:
            f.extractall()


def kaggle_download(user_dataset, file_name, competition=False):
    if competition:
        api.competition_download_file(user_dataset, file_name)
    else:
        api.dataset_download_file(user_dataset, file_name) 
    unzip_file(file_name)
        


    
