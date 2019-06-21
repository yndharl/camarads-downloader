while(1){
    if((tasklist | Select-String python).Length -eq 0)
    {
        ./skipper.ps1
    }
    Start-Sleep 60
}