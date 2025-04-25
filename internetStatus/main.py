import internet_check
import datetime
import os
import time

FILE = os.path.join(os.getcwd(), "newtworkinfo.log ")

def main():
    monitor_start_time = datetime.datetime.now()
    
    # Start monitoring internet status
    monitoring_date_time = "Monitoring begins at: " + str(monitor_start_time).split(".")[0]
    
    if internet_check.first_check():
        # If active
        print(monitoring_date_time)
        
    else:
        # If inactive
        
        while True:
            if not internet_check.ping():
                time.sleep(1)
            else:
                internet_check.first_check()
                print(monitoring_date_time)
                break
            with open(FILE, "a") as file:
                file.write("\n")
                file.write(monitoring_date_time + "\n")
    while True:
        if internet_check.ping():
            time.sleep(5)
        else:
            down_time = datetime.datetime.now()
            fail_msg = "disconnected at: " + str(down_time).split(".")[0]
            print(fail_msg)
            with open(FILE, "a") as file:
                file.write(fail_msg + "\n")
            while not internet_check.ping():
                ## Will run until connection established
                time.sleep(5)
                
            up_time = datetime.datetime.now()
            uptime_message = "Connected again: " + str(up_time).split(".")[0]
            down_time = internet_check.calculate_down_time(down_time, up_time)
            unavailabilty_time = "Connection was unavailable for: " + down_time
            print(uptime_message)
            print(unavailabilty_time)
            
            with open(FILE, "a") as file:
                file.write(uptime_message + "\n")
                file.write(unavailabilty_time, + "\n")            
            
