import subprocess
import sys

##process = subprocess.Popen(
##    "ca.exe https://www.ynet.co.il/home/0,7340,L-8,00.html", stdout=subprocess.PIPE, stderr=subprocess.PIPE
##)

process = subprocess.run(
    "ca.exe https://www.ynet.co.il/home/0,7340,L-8,00.html", stdout=subprocess.PIPE, stderr=subprocess.PIPE
)

##process = subprocess.run(
##    "dir", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
##)

print(process.stdout)

