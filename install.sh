#!/usr/bin/bash
echo "[✔] Installing ...";
echo "";
mkdir /usr/share/doc/main_g
git clone https://github.com/FahadAkash/main_game.git /usr/share/doc/main_g;
echo "";
mv /usr/share/doc/main_g/maingame /usr/bin/
chmod +x /usr/bin/maingame;
echo "Install Completed [+] Now Run On Terminal maingame"



