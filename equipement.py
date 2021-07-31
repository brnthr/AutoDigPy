#!/bin/python
import os
import subprocess
import shlex
import time

#les fichier txt
f = open("Equipement.txt", "r")
fileKO = open("EquipementKO.txt", "a+")
fileOK = open("EquipementOK.txt", "a+")

#lecture ligne par ligne
value = f.readlines()

#variable pour compter le nombre d'equipements
loopForPrint = 0
loopForFileOK = 0
loopForFileKO = 0

ligne = "_"
ligne = ligne * 40

for e in value:
   #efface les donner des deux fichier
   open("EquipementKO.txt", "w").close()
   open("EquipementOK.txt", "w").close()

   print(ligne)
   print(e)     #affiche le nom de l'equipement
   p = ".ad.testbed.dcn"
   dig = "dig +short "
   #affectue la commande dig et ajoute .ad.testbed.dcn a la suite de l'equipement
   x = os.system(dig + e.rstrip() + p)

   proc = subprocess.Popen(["dig +short " + e.rstrip() + p], stdout=subprocess.PIPE, shell=True)
   (out, err) = proc.communicate()
   ip = (out)

   loopForPrint = loopForPrint + 1

   #time.sleep(1.1)

   #condition si l'equipement n'a pas d'ip alors on write in fileKO, si il a une ip  alors write in fileOK.

   if not ip :
      fileKO.writelines(e)
      #varIpKO = e + e
      loopForFileKO = loopForFileKO + 1
      #print(varIpKO)

   else :
      fileOK.writelines(e.rstrip()+ " : "  + ip)
      #varIpOK = e + e
      loopForFileOK = loopForFileOK + 1
      print(e.rstrip()+ ":" +ip)
      #print(varIpOK)



   print("file OK : ", loopForFileOK)
   print("file KO : " , loopForFileKO)
   print("file TOTAL : ", loopForPrint)
   print(ligne)

f.close()
fileKO.close()
fileOK.close()