#!/bin/sh
# Install vim
sudo apt-get install vim-gnome -y
# Install chrome
sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -
sudo apt-get update
sudo apt-get install google-chrome-stable -y
# Install python-pip
sudo apt install python3-pip
sudo apt-get install -y python-pip
sudo apt-get install -y python-setuptools m2crypto
sudo ln -s  /usr/bin/python2 /usr/bin/py
sudo ln -s  /usr/bin/python3 /usr/bin/py3
# Install fcitx 
sudo apt-get install fcitx
sudo apt install -y fcitx-pinyin            # 拼音
# Install shadowsocks
sudo pip install shadowsocks
# Install git
sudo apt install git -y
# Autorun
sudo cp /home/geek/demoClub/linux/config/rc.local /etc/rc.local
