#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import random

banner_1 = """
                         __________
\033[36m                       .~#########%%;~.  Fahad Akash
                      /############%%;`\
         
                    |#######\    /;;;;.,.|
                    |#########\/%;;;;;.,.|
           XX       |##/~~\####%;;;/~~\;,|       XX
         XX..X      |#|  o  \##%;/  o  |.|      X..XX
        XX.....X     |##\____/##%;\____/.,|     X.....XX
  XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX Bangladesh Hacker
 X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
 X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X
 X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X
  X# \.X        @#%,.@                  @#%,.@        X./  #
   ##  X          @#%,.@              @#%,.@          X   #
 , "# #X            @#%,.@          @#%,.@            X ##
    `###X             @#%,.@      @#%,.@             ####'
   . ' ###              @#%.,@  @#%,.@              ###`"
     . ";"                @#%.@#%,.@                ;"` ' .
       '                    @#%,.@                   ,.
       ` ,                @#%,.@  @@                `
                           @@@  @@@
\033[32;1m___________________________________________________________________________
|........................Made by Fahad Akash .............................|
|.......................version 1.0.......................................|
|.......................Love You All My Subscriber........................|
|_________________________________________________________________________|
"""

bannner_2 = """
   \033[31m  _______________                        |*\_/*|________
    |  ___________  |     .-.     .-.      ||_/-\_|______  |
    | |           | |    .****. .****.     | |           | |
    | |   0   0   | |    .*****.*****.     | |   0   0   | |
    | |     -     | |     .*********.      | |     -     | |
    | |   \___/   | |      .*******.       | |   \___/   | |
    | |___     ___| |       .*****.        | |___________| |
    |_____|\_/|_____|        .***.         |_______________| Data Is Beautiful
      _|__|/ \|_|_.............*.............._|________|_
     / ********** \                          / ********** \\

"""

bannner_3 = """


 \033[36m███▄ ▄███▓ ▄▄▄       ██▓ ███▄    █   ▄████  ▄▄▄       ███▄ ▄███▓▓█████ 
▓██▒▀█▀ ██▒▒████▄    ▓██▒ ██ ▀█   █  ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
▓██    ▓██░▒██  ▀█▄  ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   
▒██    ▒██ ░██▄▄▄▄██ ░██░▓██▒  ▐▌██▒░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
▒██▒   ░██▒ ▓█   ▓██▒░██░▒██░   ▓██░░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░   ▒ ▒  ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░░   ░ ▒░  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
░      ░     ░   ▒    ▒ ░   ░   ░ ░ ░ ░   ░   ░   ▒   ░      ░      ░   
       ░         ░  ░ ░           ░       ░       ░  ░       ░      ░  ░
                                                                        
\033[32;1m
                      --{Created By : Fahad-Akash}--
                  --{Subscribe Now My YouTube Channel}--
                           --{FahadAkash}--
"""

bannner_4 = """
  \033[31m                                .
     .              .   .'.     \   /
   \   /      .'. .' '.'   '  -=  o  =-
 -=  o  =-  .'   '              / | \
   / | \                          |
     |                            |
     |                            |
     |                      .=====|
     |=====.                |.---.| ++>
     |.---.|                ||=o=||
     ||=o=||                ||   ||		\033[32mDevelop your own Mind\033[31m 
     ||   ||                ||   ||
     ||   ||                ||___|| ++>
     ||___||                |[:::]|
     |[:::]|                '-----'
     '-----'
"""
bannner_5 = """
 
 \033[34m __   __  _______  ___   __    _          _______  _______  __   __  _______ 
|  |_|  ||   _   ||   | |  |  | |        |       ||   _   ||  |_|  ||       |
|       ||  |_|  ||   | |   |_| |        |    ___||  |_|  ||       ||    ___|
|       ||       ||   | |       |        |   | __ |       ||       ||   |___ 
|       ||       ||   | |  _    |        |   ||  ||       ||       ||    ___|
| ||_|| ||   _   ||   | | | |   | _____  |   |_| ||   _   || ||_|| ||   |___ 
|_|   |_||__| |__||___| |_|  |__||_____| |_______||__| |__||_|   |_||_______|

"""



def banner():
  ser = [banner_1,bannner_2,bannner_3,bannner_4,bannner_5]
  ster = random.choice(ser)
  print(ster)


