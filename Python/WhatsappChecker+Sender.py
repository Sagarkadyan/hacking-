#Coded By @donussef
###Join https://t.me/freespamtools2

##Nigga Don't Steal it, Upgrade it

def sendout():
    import time
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from urllib.parse import urljoin
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import pyautogui
    import random
    print(f"Started on {time.asctime()}")
    print("Coded By @donussef")
    list = input("Enter List>")
    subject = input("Enter Subject > ")
    nums = open(list,"r")
    num = nums.readlines()
    sleep = int(input("Sleeping time?>"))
    web = webdriver.Chrome(ChromeDriverManager().install())
    web.get('https://web.whatsapp.com/')
    time.sleep(25)
    for numbers in num:

        try:
            fs = f"{numbers}&text=hey"
            links = urljoin("https://web.whatsapp.com/send?phone=",fs)
            link = f"https://web.whatsapp.com/send?phone={numbers}&text={subject}"
            web.get(link)

            time.sleep(sleep)
            pyautogui.press('enter')

            print("Sent > "+numbers)
            save = open("sent-logs.txt" ,"a")
            saves = save.write(numbers+"\n")
        except:
            print("Error > "+numbers)

def checker():
    import time
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from urllib.parse import urljoin
    from selenium.webdriver.common.keys import Keys
    import pyautogui
    from selenium.webdriver.common.by import By
    import random
    print("Started on {time.asctime()}")
    print("Coded By  @donussef")
    list = input("Enter List>")

    nums = open(list,"r")
    num = nums.readlines()
    web = webdriver.Chrome(ChromeDriverManager().install())
    web.get('https://web.whatsapp.com/')
    time.sleep(15)
    for numbers in num:
        try:
            fs = f"{numbers}&text=hey"
            links = urljoin("https://web.whatsapp.com/send?phone=",fs)
            link = f"https://web.whatsapp.com/send?phone={numbers}"
            web.get(link)

            time.sleep(6)
            try:
             web.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')

             print("Valid > "+numbers)
             save = open("Valid-wtssp.txt" ,"a")
             saves = save.write(numbers)
            except:
             print("Invalid Whatssap Number" +numbers)
        except:
            print("error"+numbers)

banner = '''
#FSOCIETY   ____          _          _   ____
 / ___|___   __| | ___  __| | | __ ) _   _
| |   / _ \ / _` |/ _ \/ _` | |  _ \| | | |
| |__| (_) | (_| |  __/ (_| | | |_) | |_| |
 \____\___/ \__,_|\___|\__,_| |____/ \__, |
                                     |___/
 _   _               __
| | | |___ ___  ___ / _|
| | | / __/ __|/ _ \ |_
| |_| \__ \__ \  __/  _|
 \___/|___/___/\___|_|
'''
print(banner)
print("##############TELEGRAM : @donussef")
print("1 : checker")
print("2: Sender")
option = int(input("Option >"))
if option ==1:
 checker()
elif option == 2:
 sendout()
