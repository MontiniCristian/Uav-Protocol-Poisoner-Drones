#!/usr/bin/python

#This program can be used for control a Uav.
#It was made only for domestic use, and the devolper don't trust about any costumers problems.
#Devolped by Cristian Montini , in company of ShieldOps
#    Copyright 2016 Cristian Montini.

from __future__ import print_function
from colored import fg, bg, attr
from scapy import all as scapy
import os
import time
import sys




choose = "0"
choos = "0"


def animation():
   os.system("reset")
   print("\n\n")
   print("    %s  #      #%s    %s ######%s    %s #      #%s" % (fg(196), attr(0), fg(220),attr(0), fg(81),attr(0)))
   print("    %s  #      #%s    %s#      #%s    %s#      #%s" % (fg(196), attr(0), fg(220),attr(0), fg(81),attr(0)))
   print("    %s  #      #%s    %s#      #%s     %s#    #%s" % (fg(196), attr(0), fg(220),attr(0), fg(81),attr(0)) )
   print("    %s  #      #%s    %s########%s      %s#  #%s "% (fg(196), attr(0), fg(220),attr(0), fg(81),attr(0)))
   print("    %s  ########%s @  %s#      #%s  @    %s##%s   @   %s[Protocol Poisoner]%s"% (fg(196), attr(0), fg(220),attr(0), fg(81),attr(0),fg(142), attr(5)))
   sys.stdout.write("   ")
   for i in range(64):
    time.sleep(0.02)
    sys.stdout.write("%s_%s" % (fg(6),attr(0)))
    sys.stdout.flush()
   print("%s\n\n\n%s" % (fg(2), attr(0)))

def draw():

   os.system("clear")
   print("\n\n")
   print("    %s  #      #%s    %s ######%s    %s #      #%s" % (fg(196), attr(0), fg(220),attr(0), fg(81),attr(0)))
   print("    %s  #      #%s    %s#      #%s    %s#      #%s" % (fg(196), attr(0), fg(220),attr(0), fg(81),attr(0)))
   print("    %s  #      #%s    %s#      #%s     %s#    #%s" % (fg(196), attr(0), fg(220),attr(0), fg(81),attr(0)) )
   print("    %s  #      #%s    %s########%s      %s#  #%s "% (fg(196), attr(0), fg(220),attr(0), fg(81),attr(0)))
   print("    %s  ########%s @  %s#      #%s  @    %s##%s   @   %s[Protocol Poisoner]%s"% (fg(196), attr(0), fg(220),attr(0), fg(81),attr(0),fg(142), attr(5)))
   print("%s  ________________________________________________________________%s" % (fg(6),attr(0)))
   print("%s\n\n\n%s" % (fg(2), attr(0)))

def main():
   print(" [1] TOOLS")
   print(" [2] Uav Control")
   print(" [3] Uav's Documentation")
   
   print("\n [99] Exit\n")

def tools():
  draw()
  print (" [1] Take Wlan0 --> MonitorMode")
  print (" [2] See Uav Traffic")
  print (" [3] Start Sniff Commands ")
  print (" [4] Check Interfaces")

  print("\n [99] Exit\n")

def documentation():
  draw()
  print(" [1] Uav Introduction")
  print(" [2] Uav kinds")

  print("\n [99] Exit\n")





animation()

main()









while choose != "99":
    

  if choose == "1":
    tools()
    choos = raw_input("%s[%s%sUav_Tools%s%s]>>>%s "%(fg(1), attr(4),fg(6), attr(0),fg(1), attr(0) ) )
    
    while choos != "99":
      if choos == "1":
        os.system("./airmon")
        os.system("./checkkill")
        os.system("./airmon")
        os.system("./checkkill")
        draw()
        tools()
    

      if choos == "2":
        os.system("./tcpuav")
        draw()
        tools()
        
      if choos == "3":
        animation()
        os.system("python ./CmdSniff.py")
        draw()
        tools()
  

      if choos == "4":
        os.system("ifconfig")
        raw_input("Press Enter for Exit...")
        draw()
        tools()
      
      choos = raw_input("%s[%s%sUav_Tools%s%s]>>>%s "%(fg(1), attr(4),fg(6), attr(0),fg(1), attr(0) ) )
    

    draw()
    main()

  if choose == "3":
    documentation()
    choos = raw_input("%s[%s%sINFO%s%s]>>>%s "%(fg(1), attr(4),fg(6), attr(0),fg(1), attr(0) ) )
    while choos != "99":
      if choos == "1":
        
        os.system("nano Uavs.txt")

      choos = raw_input("%s[%s%sINFO%s%s]>>>%s "%(fg(1), attr(4),fg(6), attr(0),fg(1), attr(0) ) )

    draw()
    main()

  choose = raw_input("%s[%s%sUav%s%s]>>>%s "%(fg(1), attr(4),fg(6), attr(0),fg(1), attr(0) ) )
  
    
os.system("exit")


