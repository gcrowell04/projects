### Script to monitor Internet Connnectivity
import socket
import os
import datetime

FILE = os.path.join(os.getcwd(), "newtworkinfo.log ")

def ping():
    try:
        socket.setdefaulttimeout(3)
        
        # AF_INET: address faimly for IPv4
        # SOC_STREAM: type for TCP Port
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        host = "8.8.8.8" # Google DNS
        port = 53
        
        server_address = (host,port)
        
        # Attempt to connect to the server
        s.connect(server_address)    
        
    except OSError as error:
        # Connection failed. No connection to the server.
        return False
        
        
    else:
        
        # Connection is closed after machine connects. 
        s.close()
        return True
    
def calculate_down_time(start, stop):
    
    # Calculate downtime
    downtime = stop - start
    seconds = float(str(downtime.total_seconds()))
    return str(datetime.timedelta(seconds=seconds)).split(".")[0]


def first_check():
    
    # Active check for previous connection
    if ping():
        live = "\nConnection received\n"
        print(live)
        connection_received_time = datetime.datetime.now()
        acquiring_message = " Received connection at: " + str(connection_received_time).split(".")[0]
        print(acquiring_message)
        
        # Write data to log
        with open(FILE, "a") as file:
            file.write(live)
            file.write(acquiring_message)
            return True
    else:
        not_live = "\nNo Connection received\n"
        print(not_live)
        
        # Writes into the log 
        with open(FILE, "a") as file:
            file.write(not_live)
        return False
