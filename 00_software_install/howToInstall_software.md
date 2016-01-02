#Software installation

#Objective
step of install different software

#Requirement
1. Whatever, first "sudo apt-get update sudo apt-get upgrade";

#Content
##Node.js
1. "sudo apt-get update sudo apt-get upgrade";
2. add apt resource, in console "curl -sL https://deb.nodesource.com/setup | sudo bash -";
3. install nodejs, in console "sudo apt-get install nodejs";
4. reboot the pi, "sudo shutdown -r now";
5. version check, "node -v", "npm -v";
6. OK;

##mysql
1. in console,"sudo apt-get update sudo apt-get upgrade";
2. in console, "sudo apt-get install mysql-server python-mysqldb";
3. OK, and for more [link](http://raspberrywebserver.com/sql-databases/using-mysql-on-a-raspberry-pi.html) and [link](http://www.raspberry-projects.com/pi/software_utilities/mysql), and [link](http://elinux.org/RPi_MySQL), and [link](http://dev.mysql.com/doc/refman/5.5/en/sql-syntax.html);


##mongodb
1. shortcut, download and unzip the file in Pi, run "sudo bash install.sh", [link](https://github.com/svvitale/mongo4pi);
2. dev more, [link](https://nikolayarhangelov.wordpress.com/2015/01/25/raspberry-pi-running-nodejs-and-mongodb-on-pi/), [link](http://c-mobberley.com/wordpress/2013/10/14/raspberry-pi-mongodb-installation-the-working-guide/);
3. start: /opt/mongo/bin => ./mongo

super easy, just like ghost or more copy and past
1. use pi filler(for mac) install the OS img into SD card, [headless guide](https://learn.adafruit.com/beaglebone-black-installing-operating-systems/mac-os-x)
2. For windows or other envirment, please check [link](http://www.tweaking4all.com/hardware/raspberry-pi/install-img-to-sd-card/)

#Issue
How to make own customize OS img?
