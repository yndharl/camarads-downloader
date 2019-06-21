$foldername = 'C:\Users\user\Desktop\camarads'
'starting converting'
$arr = (ls $foldername -r).fullname | Select-String -Pattern '!.*\.mp4'
$total = $arr.Length
$current = 0
foreach($in in $arr)
{
    $in = $in.ToString()
    $current++
    $out = ($in.Remove($in.Length-4)+'_cut.mp4').Replace('!','')
    ''+$current+'/'+$total
    ffmpeg -hide_banner -loglevel fatal -hwaccel cuvid -i $in -vf "select=gt(scene\,0.00001),setpts=N/(25*TB)" -an $out
    #//crop=in_w:in_h-40:0:40
    if($?)
    {
        del $in
    }
    if((ls .).name -Match 'stop')
    {
        break
    }
} 
