echo "[✔] Installing ...";
 echo "";
 mkdir /usr/bin/main_game
 git clone https://github.com/FahadAkash/main_game /usr/bin/main_game;
 echo "#!/bin/bash 
 python /usr/bin/main_game/main_game.py" '${1+"$@"}' > main_game;
 chmod +x con;
 
 
echo "Install Complete! simply run any Terminal: con"