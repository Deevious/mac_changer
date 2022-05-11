#!/usr/bin/env python

import subprocess

interface = "eth0"
new_mac = "00:11:22:33:44:77"
print("[+] Changing MAC address for " + interface + " to " + new_mac)

# Using .call to execute system commands.
# Executes 'ifconfig' + disables interface.
subprocess.call("ifconfig " + interface + " down", shell=True)

# Renaming MAC address.
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)

# Enabling MAC address.
subprocess.call("ifconfig " + interface + " up", shell=True)

