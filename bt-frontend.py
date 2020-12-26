import os
import sys
import time

def run(args):
    os.system(args)

def print_menu():
    print('[1]: List bluetooth adapters')
    print('[2]: Scan for avalible devices')
    print('[3]: Pair device')
    print('[4]: List paired devices')
    print('[5]: Connect to device')
    userin = input("? ")
    if(userin == "1"):
        run("bluetoothctl \devices")
    elif(userin == "2"):
        #print("Scanning for devices for 30 seconds!")
        print("Press CTRL-C to stop scanning")
        run("bluetoothctl \power on")
        run("bluetoothctl \scan on")
        time.sleep(30)
        run("bluetoothctl \scan off")
    elif(userin == "3"):
        mac_adress_to_pair = str(input("Enter the MAC adress you wish to pair: "))
        run("bluetoothctl \power on")
        run("bluetoothctl \pair " + mac_adress_to_pair)
    elif(userin == "4"):
        run("bluetoothctl \devices")
    elif(userin == "5"):
        mac_adress_to_connect = str(input("Enter the MAC adress you wish to connect to: "))
        run("bluetoothctl \connect " + mac_adress_to_connect)
    else:
        print("Not a vlaid command!")

running = True
while(running == True):
    print_menu()
#print(userin)
