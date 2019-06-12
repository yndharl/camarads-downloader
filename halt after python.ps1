while(1){
    if((tasklist | Select-String python).Length -eq 0)
    {
        Stop-Computer
    }
    Start-Sleep 60
}