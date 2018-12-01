import os
import shutil
delList = []
delDir = "D:/E/E/wegame/lol"
delList = os.listdir(delDir )
for f in delList:
     E = os.path.join( delDir, f )
if os.path.isfile(E):
    os.remove(E)
print(E + " was removed!")
if os.path.isdir(E):
    shutil.rmtree(E,True)
print ("Directory: " + E +" was removed!")
# os.remove('D:/E/wegame/lol/lol.exe')
