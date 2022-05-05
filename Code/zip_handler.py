from log_generator import logging
import zipfile

GENERATED_FILES = []


def generate_zip(file_list):
    try:
        with zipfile.ZipFile('Generated.zip', 'w') as new_zip:
            for files_to_zip in file_list:
                new_zip.write(files_to_zip)
    except Exception as error:
        logging.error(f'Unknown error during Zipping Operations, {error}')


def unpack_zip(zip_name):
    try:
        with zipfile.ZipFile(zip_name, "r") as zip_ref:
            zip_ref.extractall(f"Unpacked {zip_name}")
    except Exception as error:
        logging.error(f'Unknown error during Un-Zipping Operations, {error}')
