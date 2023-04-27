# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:34:31 2023

@author: jacob
"""
import datetime #13.1 Write the current date as a string to txt. file
now = datetime.date(2023, 4, 27)
now_str = now.isoformat()
with open ('today.txt', 'wt') as output:
    print(now_str, file=output)

#13.2 Read the txt. file in the string 
with open('today.txt', 'rt') as input:
    today_string = input.read()
#13.3 Parse the date form today_string'
datetime.datetime.strptime(today_string, '%Y-%m-%d\n')

#15.1 Use multiprocessing to create three separate processes. 
import multiprocessing

def current(seconds):
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())
    
if __name__ == '__main__':
    import random
    for c in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=current, args=(seconds,))
        proc.start()
