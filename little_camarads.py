import requests, re, os, time, sys, subprocess, datetime, json

vlc_path = 'C:\\Software\\VideoLAN\\VLC\\vlc.exe'
video_folder = 'C:\\Users\\user\\Desktop\\camarads'
file_len = 5 #minutes, approximately

night_mode = True
offTime = datetime.time(2,0,0) # (3:00 AM) time when downloading stop

printCams = False

# cam's IDs. For ex.: ['4_4','2_2']
download_only = [i.replace('cam','_') for i in json.loads(sys.argv[1])]
#download_only = ['4_4']

def lets_go():
    q1 = requests.get("https://www.camarads.com/")
    serv = re.findall("var serverAddr = \"(.*?)\"", q1.text)[0]
    cams = re.findall("nimbleStreamArr\['(.+?)'\] = '(.+?)'", q1.text)
    cams = dict(cams)
    if printCams:
        with open('selected_cams_%s.txt'%(str(datetime.datetime.now().date()).replace(':','-'),),'w') as w:
            w.write(str(download_only))
    if not len(download_only) == 0:
        templ = list(cams.keys())
        for i in templ:
            if i not in download_only:
                cams.pop(i)
    filename = time.strftime("!%Y-%m-%d-%H-%M-%S")
    for sel in list(cams.keys()):
        if not os.path.exists(video_folder+'\\'+sel):
            os.system('mkdir "%s\\%s"'%(video_folder,sel))
            #print("New cam!")
        if 'stop.txt' in os.listdir(video_folder+'/'+sel):
           continue
        cmd = '%s "%s" --sout="#duplicate{dst=std{access=file,mux=mp4,dst=\'%s\\%s\\%s.mp4\'},dst=nodisplay}" '%(vlc_path,serv+cams[sel],video_folder,sel,filename)
        os.popen(cmd)
        time.sleep(1)
    
print("************************************")
print("**Press Ctrl+С to stop downloading**")
print("************************************")
print('Video length = '+str(file_len))
print('Night mode = '+str(night_mode))
print("************************************")
if night_mode:
    print(offTime.strftime('%H:%M:%S'))
ctrl_c = False
lasttime = datetime.datetime.now().time()
while True:
    nowtime = datetime.datetime.now().time()
    if night_mode and lasttime < offTime and nowtime > offTime:
        break
    lasttime = nowtime
    print("Runing. Wait...")
    lets_go()
    print("Done. Now sleeping from "+str(datetime.datetime.now().time()))
    try:
        time.sleep(file_len*60)
    except KeyboardInterrupt:
        print("Exiting...")
        ctrl_c = True
    os.system('taskkill /IM "vlc.exe"')
    if ctrl_c:
        break