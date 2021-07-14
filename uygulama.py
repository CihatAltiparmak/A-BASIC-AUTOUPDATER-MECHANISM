from urllib.request import urlopen
import json

with open("version.json", "r") as f:
    version_config = json.loads(f.read())
    f.close()

url = urlopen("https://raw.githubusercontent.com/CihatAltiparmak/update_test_repository/main/version.json")
info = json.loads(url.read().decode())

if (version_config["version"] == info["version"]):
    print("güncel")
else:
    ans = input("güncelllemek ister misiniz(E/H)")
    if (ans == "E"):
        updated_app_data = urlopen(info["link"]).read()
        with open("uygulama.exe", "wb") as f:
            f.write(updated_app_data)
            f.close()
        version_config = info

with open("version.json", "w") as f:
    f.write(json.dumps(version_config))
    f.close() 
        
