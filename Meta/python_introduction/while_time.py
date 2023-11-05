import time
import datetime
import re

#create a function that checks for the time
def check_time():
    #check for the time in timestamp format
    current_time = time.time()
    #convert current time to a readable time
    current_time = datetime.datetime.fromtimestamp(current_time)
    #convert to a string
    current_time = str(current_time)
    #use regex searching to pick only the time part of it
    time_regex = r'(\d\d:\d\d):\d\d'
    time_value = re.search(time_regex, current_time)
    current_time = time_value[1]
    #create a second pause
    time.sleep(1)
    return current_time


#Type a time you want to check
input_time = input("Type the time you want to check: ")

#loop as long as the time has not changed
while check_time() == input_time:
    print("The time is currently", input_time)

#print that the loop has ended
print("Loop ended and the current time is", check_time())