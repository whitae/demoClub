#!/bin/sh
sudo apt-get install sqlite3 -y
sudo add-apt-repository ppa:linuxgndu/sqlitebrowser-testing
sudo apt-get update
sudo apt-get install sqlitebrowser
sudo apt-get install libsqlite-dev
