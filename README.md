Camarads-downloader
===================

Tool for downloading free videos from [camarads](https://camarads.com)

Requirements
------------
+ python 3
+ python libs: *flask*, *webbrowser*
+ add *python.exe* to *PATH*
+ optional ffmpeg

Usage
-----

1. Run *serv.py*, it opens the cmd window and the web page.
2. Select screenshots from cams you need.
3. Click *"Start downloading"* from the top, it opens the new cmd window and as many VLC windows as cams had been chosen.
4. Close the  python window and the web page from paragraph 1.
5. To stop downloading press *Ctrl+C* in python.

Settings
--------

You can change settings in the top of *little_camarads.py*
+ *vlc_path* Path to *vlc.exe*.
+ *video_folder* Folder where videos will be saved. It should exist.
+ *file_len* Video fragment lenght, it set how often VLC will be relaunched. Don't set too long, there are a lot of disk usage while VLC save file.
+ *night_mode* If True: downloading will stop when next video fragment will be downloaded and selected *offtime* comes.  
For ex.: 16,08,20 → 4:08:20 PM.
+ *printCams* If True: on the start *selected_cams_%time%.txt* file will be created with the list of selected cams.

Additional options
------------------

+ If you often download the same cams you can set it manually: replace value of *download_only* in *little_camarads.py* with the list of cams. See *printCams* to find it.
+ *(Does not work well)* If you want to speed up video during boring moments (without movement) run *skipper.ps1*. It remove from video some frames without difference between it. 
+ If you want to join fragments to one big file:
  1. Run in powershell in the folder with videos:
  ```
  (ls).name > input.list
  ```
  2. Edit created *input.list* to make something like:
  ```
  file 'vid1.mp4'
  file 'vid2.mp4'
  ```
  3. Run in CMD or powershell:
  ```
  ffmpeg -f concat -i input.list -c copy output.mp4
  ```
+ If you turn on *night_mode* and set *offtime* to late hour you may want to shutdown PC after end of downloading. So start *halt after python.ps1*, it will shutdown PC when all python.exe processes will be terminated.
