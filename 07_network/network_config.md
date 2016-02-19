#network config

#Objective
how to set static/dynamic ip
how to use wifi

#Requirement


#Content
###1. set static/dynamic ip
  backup the default file
  ```
  pi@raspberry: sudo cp /etc/network/interfaces /etc/network/interfaces.sav
  ```

  modify the file
  ```
  pi@raspberry: sudo nano /etc/network/interfaces
  ```

  sample file
  ```  
      auto lo
      iface lo inet loopback

      auto eth0
      allow-hotplug eth0
      iface eth0 inet dhcp#this is for dynamic
      #iface eth0 inet manual
      #iface eth0 inet static
            pre-up /etc/firewall-openvpn-rules.sh

      auto wlan0
      allow-hotplug wlan0
      iface wlan0 inet dhcp
      #iface wlan0 inet manual
      wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

      auto wlan1
      allow-hotplug wlan1
      iface wlan1 inet dhcp
      #iface wlan1 inet manual
      wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf


      #next is new add, comment out for static ip
      #address [192.168.199.173]
      #netmask [255.255.255.0]
      #network [192.168.199.0]
      #broadcast [192.168.199.255]
      #gateway [192.168.199.1]
  ```

  restart network
  ```
   pi@raspberry:sudo /etc/init.d/networking reload
  ```

###2. set wifi
  plug in wifi

  search net
  ```
  pi@raspberry: sudo iwlist wlan0 scan
  ```

  find target net,
    ESSID:"your target new"

  setting the file
  ```
  sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
  ```
  add this at bottom
  ```
  network={
      ssid="your target new"
      psk="netPassword"
  }
  ```

#Issue
debian have GUI network setting
