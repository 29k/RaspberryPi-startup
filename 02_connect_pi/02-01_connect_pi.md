#Connect Pi

#Objective
Howto Connect Pi with net-cable

#Requirement
1. Pi and Mac should connect in the same network(direct connect, or connect in the same router both OK).
2. Pi Password(default name:pi, password:raspberry)
3. get Pi Ip address(check router information).

#Content
##Connect via ssh
1. In Terminal, "ssh pi@#yourPiAddress#", then input the password. e.g."ssh pi@192.168.0.23"
2. Now you login the pi console.

##Connect via remote Desktop VNC
1. update the pi, in Pi Console "sudo apt-get update";
2. install vncserver, in Pi console "sudo apt-get install tightvncserver";
3. run vncserver on Pi, in Pi console "vncserver :1", and input the password;
4. run client on Mac, in desktop Menu line => Go => Connect to server(shortcut: command+K);
5. follow step4, input "vnc://192.168.0.23:5901";
6. tips: how 5901 came from , 5901 = 59+01, 59 is forever and 01 is from "vncserver :1";
7. stop the vncserver, "vncserver -kill :1";
7. information about tightvncserver[link](http://www.tightvnc.com/vncserver.1.php)

1. use pi filler(for mac) install the OS img into SD card, [headless guide](https://learn.adafruit.com/beaglebone-black-installing-operating-systems/mac-os-x)
2. For windows or other envirment, please check [link](http://www.tweaking4all.com/hardware/raspberry-pi/install-img-to-sd-card/)

#Issue
How to make own customize OS img?
