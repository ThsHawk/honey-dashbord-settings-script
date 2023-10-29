import sys
import json

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    print("Err: File not found.")

data = json.load(file)
file.close()

data2 = data.get("services")

for i in range(len(data2)):
    print(data2[i]["name"])
    
#data3.get
