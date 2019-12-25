#!/usr/bin/env python
import subprocess
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface whose MAC Address is to be changed")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC Address")
    ( values, arguments ) = parser.parse_args() #the method returns the values given and arguments
    if not values.interface:
        parser.error("Please specify an interface. For more help use --help")
    elif not values.mac:
        parser.error("Please specify a new mac address. For more help use --help")
    return values

def change_mac(interface, mac):
    print("[+] Changing mac address of the interface " + interface + " to " + mac) 
    subprocess.call(["ip", "link", "set", "dev", interface, "down"])
    subprocess.call(["ip", "link", "set", "dev", interface, "address", mac])
    subprocess.call(["ip", "link", "set", "dev", interface, "up"])


values = get_args()
change_mac(values.interface, values.mac)
