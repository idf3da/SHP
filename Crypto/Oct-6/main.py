from crypto import *
from os import system as execute
from platform import system as os_name

def clear():
    if os_name == "Windows": execute("cls")
    else: execute("clear")

clear()

print("This is the Ultimate Decryptor v1.0.")
thing = []
choice = 0
c = 0
thing.append(input("Input THE THING you wish to decrypt.\nIf it's an integer/binary/string or else just paste it.\nCross you fingers for it not to have any '\\n'.\nTHE THING: "))
clear()

options = '''
    dn) Dec2Nth
    nd) Nth2Dec
    bd) Bin2Dec
    db) Dec2Bin
    dr) Dec2Rus
    rd) Rus2Dec
    c) Chunk by N
    E) Decode Elias2Dec
    sb) Str2bin
split) Split by "smth"
   rev) Reverse ( 123 -> 321 )
    j) Join arr elements in str
    b) Revert previous operation
    q) Quit
    p) Print THE THING
   FW) Write THE THING to the file'''

while True:
    clear()

    ####################
    ####### DEBUG ######
    ####################
    
    print(thing)

    ####################
    ####################

    print("@>>> Oll Korrect.")
    print("@>>> Iteration Num:", c)
    print("@>>> This is your thing:\n\n", thing[c],"\n")
    print("@>>> It's type is", type(thing[c]))
    print("@>>> What would you like to do?")
    print(options)
    choice = input("@>> Your choice: ")
    if choice == "q":
        clear()
        exit()
    elif choice == "p":
        clear()
        print("\n\n")
        print(*thing[c], sep='')
        print("\n\n")
        input("Press Enter")
    elif choice == "b":
        if c:
            c -= 1
            thing.pop()
        else:
            print("No operation to revert!")
            input("Press Enter")
    elif choice == "split":
        by = input("Split by: ")
        thing.append(thing[c].split(by))
        c += 1
    
    elif type(thing[c]) == list:
        res = []
        if choice == "dn":
            n = input("Nth base: ")
            for z in thing[c]:
                res.append(dec2nth(z, n))
        elif choice == "nd":
            n = input("Nth base: ")
            for z in thing[c]:
                res.append(nth2dec(z, n))
        elif choice == "bd":
            for z in thing[c]:
                res.append(bin2dec(z))
        elif choice == "db":
            for z in thing[c]:
                res.append(dec2bin(z))
        elif choice == "dr":
            for z in thing[c]:
                res.append(dec2rus(z))
        elif choice == "rd":
            for z in thing[c]:
                res.append(rus2dec(z))
        elif choice == "c":
            pass
        elif choice == "E":
            for z in thing[c]:
                res.append(elias2dec(z))
        elif choice == "9":
            a = input("1 for: ")
            b = input("and 0 for: LOL don't care")
            for z in thing[c]:
                res.append(str2bin(z, a))
        elif choice == "split":
            pass
        elif choice == "j":
            res = "".join(thing[c])
        else:
            print("FATAL ERROR")
            exit()
        c += 1
        thing.append(res)

    elif type(thing[c]) == str:
        if choice == "dn":
            n = input("Nth base: ")
            res = dec2nth(thing[c], n)
        elif choice == "nd":
            n = input("Nth base: ")
            res = nth2dec(thing[c], n)
        elif choice == "bd":
            res = bin2dec(thing[c])
        elif choice == "db":
            res = dec2bin(thing[c])
        elif choice == "dr":
            res = dec2rus(thing[c])
        elif choice == "rd":
            res = rus2dec(thing[c])
        elif choice == "c":
            n = input("Num of chunks: ")
            res = list(chunk(thing[c], n))
        elif choice == "E":
            res = elias2dec(thing[c])
        elif choice == "sb":
            a = input("1 for: ")
            b = input("and 0 for: LOL don't care")
            res = str2bin(thing[c], a)
        elif choice == "split":
            smthn = input("Smnth: ")
            res = choice[c].split(smthn)
        elif choice == "rev":
            res = reverseArray(choice[c])
        elif choice == "j":
            res = "".join(thing[c])
        thing.append(res)
        c += 1












