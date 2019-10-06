from crypto import *
from os import system as execute
from platform import system as os_name

def clear():
    if os_name == "Windows": execute("cls")
    else: execute("clear")

print("This is Ultimate Decryptor v1.0.")
thing = input("Input THE THING you wish to decrypt.\n If it's an integer/binary/string or else just paste it: ")

print(thing)