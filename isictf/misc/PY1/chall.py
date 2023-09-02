from sys import exit
import os

blacklist = "0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"
Flag = os.environ.get("FLAG", "FLAG{this_is_a_fake_flag}")

if __name__ == "__main__":
    while True:
        var = input("Welcome to eval service")
        if var == "Flag":
            print("Nice try!")
        elif var == "exit":
            exit()
        elif any(bad in var for bad in blacklist):
            print("Hacking attempt detected!")
        else:
            try:
                print(eval(var))
            except:
                print("Your are trying to break my program")