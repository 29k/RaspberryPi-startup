#Setup vpn server

#FAIL, need static ip address

#Objective
Guide for VPN setup on PI

#Requirement
1. a system installed Pi

#Content
###Set the PI static ip address
  1. check ip address
    ```
    ifconfig
    ```
    write down the address and mask and bcast
    look like
    ```
    inet addr:192.168.199.173  Bcast:192.168.199.255  Mask:255.255.255.0
    ```

  2. check route
    ```
    sudo route -n
    ```
    write down the destination and gateway
    look like
    ```
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    0.0.0.0         192.168.199.1   0.0.0.0         UG    202    0        0 eth0
    192.168.199.0   0.0.0.0         255.255.255.0   U     202    0        0 eth0
    ```

  3. set the config file
    ```
    sudo nano /etc/network/interfaces
    ```

    change the content into
    ```
    auto lo
    iface lo inet loopback

    auto eth0
    allow-hotplug eth0
    #iface eth0 inet manual
    iface eth0 inet static

    auto wlan0
    allow-hotplug wlan0
    iface wlan0 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

    auto wlan1
    allow-hotplug wlan1
    iface wlan1 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

    #next is new add
    address [192.168.199.173]
    netmask [255.255.255.0]
    network [192.168.199.0] #this is destination
    broadcast [192.168.199.255]
    gateway [192.168.199.1]
    ```

  4. install openvpn
    ```
    sudo apt-get update && sudo apt-get upgrade
    sudo apt-get install openvpn
    ```

  5. set rsa file
    ```
    sudo cp -r /usr/share/doc/openvpn/examples/easy-rsa/2.0 /etc/openvpn/easy-rsa
    sudo nano /etc/openvpn/easy-rsa/vars
    ```
    modify the line into
    ```
    export EASY_RSA="/etc/openvpn/easy-rsa"
    ```
    create certifcates
    ```
    cd /etc/openvpn/easy-rsa
    sudo -s
    source ./vars
    ./clean-all
    ./build-ca
    ./build-key-server [ServerName]
    ```
    and press "y" "y"

    build user_key
    ```
    ./build-key-pass [UserName]
    cd keys
    openssl rsa -in yourname.key -des3 -out yourname.3des.key
    cd ..
    ./build-dh
    openvpn --genkey --secret keys/ta.key
    ```

#Issue
