from urllib.request import urlopen
import json
from zipfile import ZipFile
import os
import shutil

APP_AUTHOR = "CihatAltiparmak"
APP_NAME = "A-BASIC-AUTOUPDATER-MECHANISM"
APP_BRANCH = "main"


VERSION_LINK = "https://raw.githubusercontent.com/" + APP_AUTHOR + "/" + APP_NAME + "/" + APP_BRANCH+ "/version.json"
APP_DIR = os.path.realpath(".")


class Starter:
    def __init__(self):
        self.latest_info = self.get_latest_info()
        self.current_info = self.get_current_info()

        if (self.is_update()):
            print("App has got the latest version.")
        else:
            print("[Started Updating Process]")
            self.update()
            print("[Finished Updating Process]")
            self.save_changes()
        
        import app        
        app.start_application()

    def get_latest_info(self):
        url = urlopen(VERSION_LINK)
        latest_info = json.loads(url.read().decode())
        return latest_info

    def get_current_info(self):
        try:
            with open("version.json", "r") as f:
                current_info = json.loads(f.read())
            return current_info
        except FileNotFoundError:
            # if version.json was deleted during updating, 
            # It means that some problems such as shutdown suddenly of computer occured during updating 
            return {"version" : "", "link" : ""}

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
        link = self.latest_info["link"]
        updated_app_data = urlopen(link).read()
        with open(zip_file_path, "wb") as f:
            f.write(updated_app_data)

    def reconfigure_dirs(self, zip_file_path):
        with ZipFile(zip_file_path, 'r') as zip_file:
            zip_file.extractall(".cache")
            """
            default branch is main, in downloaded zip, file tree is like this:
            For Example:
            A-BASIC-AUTOUPDATER-MECHANISM-main
            ├── app_gui.py
            ├── app_gui.ui
            ├── app.py
            ├── main.py
            ├── README.md
            └── version.json
            so cache dir  should be .cache/($APP_NAME)-($APP_BRANCH)
            """
            CACHE_DIR = os.path.join(APP_DIR, ".cache" , APP_NAME + "-" + APP_BRANCH)
            for _dir in os.listdir(CACHE_DIR):
                if _dir != "main.py":
                    old_path = os.path.join(CACHE_DIR, _dir)
                    new_path = os.path.join(APP_DIR, _dir)
                    os.rename(old_path, new_path)

    def is_update(self):
        return self.current_info["version"] == self.latest_info["version"] 
    
    def save_changes(self):
        if not self.is_update():
            self.current_info = self.latest_info

        with open("version.json", "w") as f:
            f.write(json.dumps(self.current_info, indent = 4))

if __name__ == "__main__":
    Starter()       
