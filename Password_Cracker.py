



        ###################
        # code by Teslaw  #
        ###################


import itertools
import hashlib
import os.path


def crack_with_file():

    hash_mode = None # ------------------------------------------------------------------

    while hash_mode == None :

        text = "\nYou can enter exit to end it !\n\nSelect one of them this hash types : \n\n0. auto Detect \n1. sha1 \n2. sha256 \n3. sha224 \n4. sha384 \n5. sha 512 \n6. md5 \n\nEnter mode number :"
        mode = input(text)

        if mode == "0" :
            hash_mode = "Auto Detecting"
        elif mode == "1":
            hash_mode = "sha1"
        elif mode == "2":
            hash_mode = "sha256"
        elif mode == "3":
            hash_mode = "sha224"
        elif mode == "4":
            hash_mode = "sha384"
        elif mode == "5":
            hash_mode = "sha512"
        elif mode == "6":
            hash_mode = "md5"
        elif mode == "exit":
            quit()
        else :
            print("\ncommand error ! [Enter a leagal command]\n")


    print(f"\n[{hash_mode}]  Selected")

    hash_self = None # ------------------------------------------------------------------
    while hash_self == None :
        hash = input("\nEnter Hash :")
        if hash_mode == "Auto Detecting" :
            len_hash = len(hash)

            if len_hash == 32 :
                if hash.strip() :
                    hash_self = hash.strip().lower()
                    hash_mode = "md5"

            elif len_hash == 40 :
                if hash.strip() :
                    hash_self = hash.strip().lower()
                    hash_mode = "sha1"

            elif len_hash == 56 :
                if hash.strip() :
                    hash_self = hash.strip().lower()
                    hash_mode = "sha224"

            elif len_hash == 64:
                if hash.strip():
                    hash_self = hash.strip().lower()
                    hash_mode = "sha256"

            elif len_hash == 96:
                if hash.strip():
                    hash_self = hash.strip().lower()
                    hash_mode = "sha384"

            elif len_hash == 128:
                if hash.strip():
                    hash_self = hash.strip().lower()
                    hash_mode = "sha512"

            elif hash == "exit":
                quit()
            else:
                print("\nNo entry ! [please enter hash]")
        else:
            if hash.strip():
                hash_self = hash.strip().lower()
            elif hash == "exit":
                quit()
            else:
                print("\nNo entry ! [please enter hash]")

        print(f"\n[{hash_mode}]  Detected")



    file = None # ------------------------------------------------------------------

    while file == None:
        file_entry = input("\nEnter file name or directory :")

        if os.path.isdir(file_entry) == True or os.path.isfile(file_entry) == True:
            file = file_entry
        elif os.path.isdir(file_entry) == False or os.path.isfile(file_entry) == False:
            print("File or directory not found [Wrong address]")
        elif file_entry == "exit":
            quit()

    found_password = None # -----------------------------------------------------------
    file = open(file)
    for line in file:
        if line.strip().rstrip() != "":
            print(f"Testing \t [ {line.strip()} ]")

            encoded1 = line.strip().rstrip()
            encoded = encoded1.encode("utf-8")

            if hash_mode == "sha1" :
                hashed = hashlib.sha1(encoded)
                if hashed.hexdigest() == hash_self:
                    found_password = line
                    break

            if hash_mode == "sha224":
                hashed = hashlib.sha224(encoded)
                if hashed.hexdigest() == hash_self:
                    found_password = line
                    break

            if hash_mode == "sha256":
                hashed = hashlib.sha256(encoded)
                if hashed.hexdigest() == hash_self:
                    found_password = line
                    break

            if hash_mode == "sha384":
                hashed = hashlib.sha384(encoded)
                if hashed.hexdigest() == hash_self:
                    found_password = line
                    break

            if hash_mode == "sha512":
                hashed = hashlib.sha512(encoded)
                if hashed.hexdigest() == hash_self:
                    found_password = line
                    break

            if hash_mode == "md5":
                hashed = hashlib.md5(encoded)
                if hashed.hexdigest() == hash_self:
                    found_password = line
                    break

    if found_password != None :
        print(f"\n \t [ Password found ] >>> {found_password}")
    else:
        print("\n \t [ Password not found ] ")



def crack_auto_generated():
    hash_mode = None # ------------------------------------------------------------------

    while hash_mode == None :

        text = "\nYou can enter exit to end it !\n\nSelect one of them this hash types : \n\n0. auto Detect \n1. sha1 \n2. sha256 \n3. sha224 \n4. sha384 \n5. sha 512 \n6. md5 \n\nEnter mode number :"
        mode = input(text)

        if mode == "0" :
            hash_mode = "Auto Detecting"
        elif mode == "1":
            hash_mode = "sha1"
        elif mode == "2":
            hash_mode = "sha256"
        elif mode == "3":
            hash_mode = "sha224"
        elif mode == "4":
            hash_mode = "sha384"
        elif mode == "5":
            hash_mode = "sha512"
        elif mode == "6":
            hash_mode = "md5"
        elif mode == "exit":
            quit()
        else :
            print("\ncommand error ! [Enter a leagal command]\n")


    print(f"\n[{hash_mode}]  Selected")

    hash_self = None # ------------------------------------------------------------------
    while hash_self == None :
        hash = input("\nEnter Hash :")
        if hash_mode == "Auto Detecting" :
            len_hash = len(hash)

            if len_hash == 32 :
                if hash.strip() :
                    hash_self = hash.strip().lower()
                    hash_mode = "md5"

            elif len_hash == 40 :
                if hash.strip() :
                    hash_self = hash.strip().lower()
                    hash_mode = "sha1"

            elif len_hash == 56 :
                if hash.strip() :
                    hash_self = hash.strip().lower()
                    hash_mode = "sha224"

            elif len_hash == 64:
                if hash.strip():
                    hash_self = hash.strip().lower()
                    hash_mode = "sha256"

            elif len_hash == 96:
                if hash.strip():
                    hash_self = hash.strip().lower()
                    hash_mode = "sha384"

            elif len_hash == 128:
                if hash.strip():
                    hash_self = hash.strip().lower()
                    hash_mode = "sha512"

            elif hash == "exit":
                quit()
            else:
                print("\nCan not Detect [Unknown Type]")
        else:
            if hash.strip():
                hash_self = hash.strip().lower()
            elif hash == "exit":
                quit()
            else:
                print("\nNo entry ! [please enter hash]")

        print(f"\n[{hash_mode}]  Detected")



    use_letters = None # --------------------------------------------------------------
    while use_letters == None :
        letters = input("\nEnter letters :")

        if letters.strip():
            use_letters = letters
        elif letters == "exit":
            quit()
        else :
            print("\n [ empty ! ]")

    repeat = None
    while repeat == None :
        inp_repeat = input("\nEnter caracter lengh :")
        if inp_repeat.strip():
            try:
                repeat = int(inp_repeat)
            except:
                print("\nError [ Enter a number please ] ")
        elif inp_repeat == "exit":
            quit()
        else:
            print("\nError [ Enter a number ]")


    start_from_one_character = None
    while start_from_one_character == None :
        ask = input("\nDo you want to start from one character [ y or n ]?")
        if ask.lower() == "y":
            start_from_one_character = "yes"
        elif ask.lower() == "n" :
            start_from_one_character = "no"
        else:
            print("\nJust enter 'y' or 'n' [ !!! ]")

    # generating words and then hashes !
    pass_txt_file = open("passwordList.txt","w")
    print("\n\n \t [ Creating password list ] >> It's because of RAM limits")
    if start_from_one_character == "no":
        for list_word in itertools.product(use_letters,repeat=repeat):
            pass_txt_file.write("".join(list_word)+"\n")
        pass_txt_file.close()

    else :
        Start = 1
        for i in range(repeat):
            for list_word in itertools.product(use_letters,repeat=Start):
                pass_txt_file.write("".join(list_word)+"\n")
            Start +=1
        pass_txt_file.close()

    found_password = None # -----------------------------------------------------------
    file = open("passwordList.txt")
    for line in file:
        if line.strip().rstrip() != "":
            print(f"Testing \t [ {line.strip()} ]")

            encoded1 = line.strip().rstrip()
            encoded = encoded1.encode("utf-8")

            if hash_mode == "sha1" :
                hashed = hashlib.sha1(encoded)
                if hashed.hexdigest() == hash_self:
                    found_password = line
                    break

            if hash_mode == "sha224":
                hashed = hashlib.sha224(encoded)
                if hashed.hexdigest() == hash_self:
                    found_password = line
                    break

            if hash_mode == "sha256":
                hashed = hashlib.sha256(encoded)
                if hashed.hexdigest() == hash_self:
                    found_password = line
                    break

            if hash_mode == "sha384":
                hashed = hashlib.sha384(encoded)
                if hashed.hexdigest() == hash_self:
                    found_password = line
                    break

            if hash_mode == "sha512":
                hashed = hashlib.sha512(encoded)
                if hashed.hexdigest() == hash_self:
                    found_password = line
                    break

            if hash_mode == "md5":
                hashed = hashlib.md5(encoded)
                if hashed.hexdigest() == hash_self:
                    found_password = line
                    break

    if found_password != None :
        print(f"\n \t [ Password found ] >>> {found_password}")
    else:
        print("\n \t [ Password not found ] ")




if __name__ == "__main__":
    text = "\n*** Enter Cracking Mode *** \n\n1. Enter Password List\n2. Auto Generate Mode\nSelect mode :"
    mode = input(text)

    if mode == "1":
        crack_with_file()
    elif mode == "2" :
        crack_auto_generated()
    else :
        print("\nCommand Not Supported")