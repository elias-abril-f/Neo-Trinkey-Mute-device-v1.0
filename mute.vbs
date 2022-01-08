Set oShell = CreateObject("WScript.Shell")

oShell.Run("rundll32.exe shell32.dll,Control_RunDLL mmsys.cpl,,recording")
WScript.Sleep(500)
oShell.AppActivate("Sound")
oShell.SendKeys("{DOWN}")
oShell.SendKeys("%p+{TAB}{RIGHT}{RIGHT}{TAB}{TAB} {TAB}{TAB}{ENTER}{ENTER}")