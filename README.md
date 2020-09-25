# obstimer

THIS PROJECT IS NOW OBSOLETE AND NOT MAINTAINED.
IMPROVED PYTHON VERSION AVAILABLE HERE: https://github.com/exenza/obspymer

obstimer via text file

Copy the repo in a user system folder (i.e. ~/Documents/obstimer)

In OBS create a "text" source that load from file and point it to "[path-to]/obstimer/timer.txt"

In your terminal navigate to the obstimer fodler and:
sudo chmod +x *.sh

On your streamdeck use the "start application" action, this the breakdown of what each script does:

timerstart.sh
Start/Pause the timer, if no timer is running will act as a stopwatch

timer1.sh / timer5.sh
Add one/five minutes to the timer while timer is running.
If timer is not running time will be added but timer will have to be started with "timestart.sh"
You can invoke this multiple time to add minutes (example invoke timer1.sh 3 times to add 3m)

timerdown5.sh
Remove 5m from running timer without pause it or start it.
If less then 5m are left nothing will happen.

timerstart15.sh / timerstart30.sh / timerstart45.sh /timerstart1h.sh 
Reset and start the timer at the respective respective time (15m / 30m / 45m / 60m)

timerreset.sh
Reset the timer

timerset.sh
Not sure file is needed, ain't smart enough to remember what I did.... but it may be removed from the repo if I confirm I don't use it :)
