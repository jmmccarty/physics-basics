#!/usr/bin/env python3
# This module will calculate the acceleration of an object based on beginging
# and ending velocity over a period of time. Initially it will only do this in 
# meters per second over a period of seconds.

import os


def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def acceleration():
    print("This module will calculate the average acceleration of an object based on initial velocity\n"
    "and final velocity over a period of seconds.")
    initial_velocity=int(input("\nWhat is the initial velocity of the object in m/s? "))
    final_velocity=int(input("\nWhat is the final velocity of the object in m/s? "))
    elapsed_time=int(input("\nHow much time has elapsed, in seconds? "))
    acceleration=(final_velocity - initial_velocity)/elapsed_time
    print("\nThe object has an acceleration of " + str(acceleration) + " m/s\xB2")
    

def main():
    input_choice=""
    clear()
    while input_choice != "n":
        acceleration()
        input_choice=input("\nWould you like to do another calculation? y/n ").lower()

main ()
