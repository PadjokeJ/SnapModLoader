import os
import shutil
os.system("echo Importing Marvel Snap mods")
file = open('path.txt', 'r+')
_path = file.read() + "\\"
modPath = os.getcwd() + "\\Mods\\"
defaultPath = os.getcwd() + "\\DefaultFiles\\"
shutil.copyfile(_path + "catalog_snap_19.18.3.json", defaultPath + "unpatched_catalog_snap_19.18.3.json")
shutil.copyfile("catalog_snap_19.18.3.json", os.path.expanduser('~') + "\\AppData\\LocalLow\\second dinner\\snap\\com.unity.addressables\\catalog_snap_19.18.3.json")
shutil.copyfile("catalog_snap_19.18.3.json", _path + "catalog_snap_19.18.3.json")
os.system("echo patched catalog file")
files = os.listdir(modPath)
for f in files:
    print(f)
    shutil.copyfile(_path + f, defaultPath + f)
    shutil.copyfile(modPath + f, _path + f)