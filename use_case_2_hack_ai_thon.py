# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:16:41 2019

@author: Satyajeet 1029693
"""

print("""
          Welcome to Bill Calculator
          --------------------------
Work hours are between 0800 hours to 2400 hours
      """)



#To get input from user, entry time and exit time
#'counter' varibale checks the number of attempts of input
def time_input(counter):
    entry_time=int(input("Enter Starting time(24 hours clock(for 12AM midnight, Enter 2400)):"))
    exit_time=int(input("Enter Exit time(24 hours clock(for 12AM midnight, Enter 2400)):"))
    validity_of_time(entry_time,exit_time)
        
#To check if the time entered by user is in valid format and between 24 hours cycle, if yes then calculate the minutes of work for that day    
def validity_of_time(entry_time,exit_time):
    global counter
    if (entry_time>2400 or exit_time>2400 or entry_time>exit_time):
        while(counter<=2):
            print("\n***ERROR time not in valid format or range Error*** Try Again")
            print("\nNumber of Attempts",counter)
            counter+=1
            time_input(counter)
            break
        
        
    else:
        entry_hours,entry_minutes=entry_time//100,entry_time%100
        start_minute=entry_hours*60+entry_minutes
        exit_hours,exit_minutes=exit_time//100,exit_time%100
        exit_minute=exit_hours*60+exit_minutes
        
        billed_minutes(start_minute,exit_minute)

#To calculate the bill as per the given condition 
#1260 is equaivalent minutes for 9PM, when child will be on bed 
#prime time is when bill rate will be 2.5$ and nonprime time is when bill rate will be 1.75$
def billed_minutes(start_minute,exit_minute):
    if(start_minute>=1260 and exit_minute>=1260):
        non_prime_time=exit_minute-start_minute
        prime_time=0
    elif(exit_minute<=1260 and start_minute<=1260):
        prime_time=exit_minute-start_minute
        non_prime_time=0
    else:
        prime_time=1260-start_minute
        non_prime_time=exit_minute-1260
        
    total_bill=2.5*(prime_time/60)+1.75*(non_prime_time/60)
    print("work while child was awake {} minutes or {} hours".format(prime_time,(prime_time/60)))
    print("work after child slept {} minutes or {} hours".format(non_prime_time,(non_prime_time/60)))
    print("total bill is : {}$".format(total_bill))

counter=1
time_input(counter) 
      
    
    
