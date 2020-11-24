import glob
import os
import requests
import sys

def _lineNotify(payload,file=None):
    url = 'https://notify-api.line.me/api/notify'
    token = str (lines[0])
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)

def notifyFile(filename):
    file = {'imageFile':open(filename,'rb')}
    payload = {'message': 'ทำการส่งรูปล่าสุด'}
    return _lineNotify(payload,file)

try:
    text_file = open("./linetoken.txt", "r")
    lines = text_file.read().split('\n')
except IOError:
    #print("File not accessible")
    with open("./linetoken.txt", "w") as txt_file:
        txt_file.write('Replace this line to LINE Notify token.')
    sys.exit()

if lines[0] == '':
    #print("err3")
    sys.exit()

list_of_jpg_files = glob.glob('./*.jpg') # * means all if need specific format then *.csv
if not list_of_jpg_files:
    #print("No Image File.(err1)")
    sys.exit()
else:
    latest_img_file = max(list_of_jpg_files, key=os.path.getctime)

if len(lines) == 1:
    lines.append('./test.jpg')

if latest_img_file == lines[1]:
    #print (latest_img_file)
    #print(lines[1])
    sys.exit()

notifyFile(latest_img_file)

data = [lines[0], latest_img_file]
with open("./linetoken.txt", "w") as txt_file:
    for line in data:
        txt_file.write(line + "\n")