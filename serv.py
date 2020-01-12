import requests
import re
import json
import sys, subprocess
import webbrowser
from flask import Flask, request, jsonify

webbrowser.open('http://127.0.0.1:8524')

app = Flask(__name__)

@app.route("/get")
def gtfo():
    return 'GTFO'

@app.route("/")
def face():
    return open('face.html').read()
    
@app.route("/jquery")
def jquery():
    return open('jquery-3.4.1.min.js').read()
    
@app.route("/js")
def js():
    return open('jsjs.js').read()
    
@app.route('/get', methods=['POST'])
def get():
    return requests.get(request.form['get']).text
    
@app.route('/getPics')
def getPics():
    fromAPI = requests.get('https://camarads.com/api_time/get_pop/0').text
    mainPage = requests.get('https://camarads.com').text
    jsonFromMain = re.findall('var GLOBALSAPPS = (.+?);', mainPage)[0]
    camNames = json.loads(jsonFromMain)
    pathPart = json.loads(fromAPI)['folderV3']
    freeCams=[]
    for pair in camNames.values():
        tmp1 = {} # every cam
        tmp1['name'] = pair['name']
        tmp2 = []
        print(pair.get('locked_rooms','qwe'+pair['name']))
        for openRoomIndex in [i for i in pair['rooms'] if int(i) not in pair.get('locked_rooms',[])]:
            tmp2.append({'title': pair['rooms'][openRoomIndex],
                        'stream': pair['stream'][openRoomIndex],
                        'preview': 'https://www.camarads.com/reallifecam-free-voyeur-house/%s/%s.jpg'%(pathPart, pair['stream'][openRoomIndex])})
        tmp1['rooms'] = tmp2
        freeCams.append(tmp1)
    #print(freeCams)
    return json.dumps(freeCams)

@app.route('/sendStreams', methods=['POST'])
def sendStreams():
    subprocess.Popen(["cmd.exe", "/c", "start", "python.exe", 'little_camarads.py', request.form['streams']])
    #p.communicate()
    shutdown_server()
    return ''

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == '__main__':
    print("*********************************")
    print("**CLOSE ME AFTER SELECTING CAMS**")
    print("*********************************")
    app.run(host = '127.0.0.1', port = 8524, debug = False)