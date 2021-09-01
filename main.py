from urllib.request import urlopen
import json
from zipfile import ZipFile
import os
import shutil

import app

class Starter:
    def __init__(self):
        self.version_link = "https://raw.githubusercontent.com/CihatAltiparmak/update_test_repository/main/version.json" 
        self.latest_info = self.get_latest_info()
        self.current_info = self.get_current_info()

        if (self.is_update()):
            print("Application is already updated.")
            app.start_application()
        else:
            print("[Started Updating Process]")
            self.update()
            print("[Finished Updating Process]")
            self.save_changes()


    def get_latest_info(self):
        url = urlopen(self.version_link)
        latest_info = json.loads(url.read().decode())
        return latest_info

    def get_current_info(self):
        with open("version.json", "r") as f:
            current_info = json.loads(f.read())
        return current_info

    def update(self): 
        self.__update_files(".cache/updated_app_data.zip")

    def __update_files(self, zip_file_path): 
        self.clear_app_dirs()
        self.fetch_data(zip_file_path)
        self.reconfigure_dirs(zip_file_path)    
        shutil.rmtree(".cache")

    def clear_app_dirs(self):
        for _dir in os.listdir():
            if (_dir == 'main.py'):
                continue
            if (os.path.isfile(_dir)):
                os.remove(_dir)
            elif (os.path.isdir(_dir)):
                shutil.rmtree(_dir)

    def fetch_data(self, zip_file_path):
        os.mkdir(".cache")
        link = "https://github.com/CihatAltiparmak/update_test_repository/archive/refs/heads/main.zip" # self.latest_info["link"]
        updated_app_data = urlopen(link).read()
        with open(zip_file_path, "wb") as f:
            f.write(updated_app_data)

    def reconfigure_dirs(self, zip_file_path):
        with ZipFile(zip_file_path, 'r') as zip_file:
            for _dir in zip_file.namelist()[1::]:
                if (_dir != 'update-test-repository-main/main.py'):
                    zip_file.extract(_dir, "..")

    def is_update(self):
        return self.current_info["version"] == self.latest_info["version"] 
    
    def save_changes(self):
        if not self.is_update():
            self.current_info = self.latest_info

        with open("version.json", "w") as f:
            f.write(json.dumps(self.current_info))

if __name__ == "__main__":
    Starter()

       
