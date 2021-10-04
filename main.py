import pyautogui
import  time
import random
import cowsay
cowsay.daemon("""
import pyautogui
import  time
import random
import cowsay
""")
intro=cowsay.ghostbusters("A spambot is a computer program designed to assist in the sending of spam. Spambots usually create accounts and send spam messages with them.".title())
logo=cowsay.dragon('welcome to spam bot version 1'.title())
print("Gui Version -----soon---".title())
number= int (input("-------->Enter your time sleep::----->".title()))
def Spam_Bot():
    print(f" hold for {number} sec".title())
    for i in range(1,number):
        time.sleep(1)
        print(f"---------->{i}--------->")

    print_message=open("mihir.txt")
    for each_line in print_message:
        pyautogui.typewrite(each_line)
        pyautogui.press("Enter")
range1=int(input("------->Enter your range: for a spam bot::---->".title()))
for i in range(1,range1):
 Spam_Bot()