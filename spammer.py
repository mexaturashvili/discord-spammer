import requests
import os
from os import system
def start():   
 from colorama import init, Fore, Style
 system("title " + 'Discord spammer')

 init (autoreset=True)
 init(convert=True)
 
 
 
 
 
 
 
 
 
 

    
 print (Fore.RED + """   _____  _                       _                                                 
  |  __ \(_)                     | |                                                    
  | |  | |_ ___  ___ ___  _ __ __| |      ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
  | |  | | / __|/ __/ _ \| '__/ _` |     / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ | '__|
  | |__| | \__ | (_| (_) | | | (_| |     \__ | |_) | (_| | | | | | | | | | | |  __| |   
  |_____/|_|___/\___\___/|_|  \__,_|     |___| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                             | |                                        
                                             |_|                                        
 \n""")
 
 print(Fore.YELLOW + "Atomexplosion LTD                                    our discod server - [https://discord.gg/ZYwBMPXk3H]  \n \n")
 input ("Press enter to continue")
 os.system('cls')
 
 print (Fore.YELLOW + "Choose spam type\n\n")
 print (Fore.RED + "Say \"1\" (DM SPAM) \n")
 print(Fore.GREEN + "   or    ")
 print (Fore.RED + "\nSay \"2\" (CHANNEL SPAM) \n")
 
 print (Fore.WHITE + Style.BRIGHT + "say \"3\" to close\n")
 DM_or_channel= int(input("Select: "))
  
 
 
 
 Style.RESET_ALL
 
 
 if DM_or_channel == 1:
   os.system('cls')
   print ('Please enter numbers after https://discord.com/channels/@me/ (more info is in our server)')
   numbers = input("number: ")
   url = "https://discord.com/api/v9/channels/"+numbers+"/messages"
   system("title " + 'Discord DM spammer')
   os.system('cls')
   
 elif DM_or_channel == 2:
   os.system('cls')
   channel_ID = input("Channel ID: ")
   url = "https://discord.com/api/v9/channels/"+channel_ID+"/messages"
   system("title " + 'Discord channel spammer')
   os.system('cls')
   
 elif DM_or_channel == 3:
   exit()
 else:
   exit()
 os.system('cls')
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 #token prompt (not grabber 100% safe)
 token = input("Discord token: ")
 os.system('cls')
 
 
 auth = { 'authorization': token
 }
 
 os.system('cls')
 
 
 #message that script will spam
 spam_message = input("Spam message: ")
 
 os.system('cls') 
 
 

 while True:
     try:
         how_many = int(input("How many messages: "))
         break
     except:
         print("invalid number")
 
 
 
 
 msg = {
 'content': spam_message
 }
 
 os.system('cls')
 
 
 
 #let the hell begin :D
 
 
 i = 1
 while i < how_many + 1:
   print('messages sent:', i, 'of', how_many )
   requests.post(url,headers = auth, data = msg)
   if (i == how_many):
     break
   i += 1
 
 print ("spam succesfully completed!")
 input ("Press enter to finish (some messages may be still sending so it's recommended to wait until spam finishes)")

 
 os.system('cls')
 start()
 return
start()
