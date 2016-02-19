#Tips

#Objective
useful tips

#Requirement
1. None

#Content
1. disable screen sleep
  install xscreensaver and in desktop config disable sleep
  install command,
  ```
  sudo apt-get update
  sudo apt-get install xscreensaver
  ```

2. hide start up boot screen
  ```
  sudo nano /boot/cmdline.txt
  ```
  - Replace "console=tty1" by "console=tty3" to redirect boot messages to the third console.
  - Add "loglevel=3" to disable non-critical kernel log messages.
  - logo.nolog, no more pi logo
  sample:
  ```
  dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty3 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait logo.nologo loglevel=3
  ```

3. autostart a function after login
###set autostart file
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
@xscreensaver -no-splash
@Lxterminal
@lxterminal -e sudo python /home/pi/Desktop/test1.py
@lxterminal -e sudo /home/pi/Desktop/autorun.sh
```

###creat autorun.sh
```
#!/bin/bash

echo Hello world

sudo python /home/pi/Desktop/logb.py

$SHELL
```

###chmode
```
sudo chmod +x autorun.sh
```

#Issue
How to make own customize OS img?
