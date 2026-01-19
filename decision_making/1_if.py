""" write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 
        input : 15 hours 
        output  3 PM
"""
hours = int(input("enter time:"))

if hours > 12 and hours <= 24:
    print((hours-12),"PM")
if hours <= 12:
    print(hours,"AM")
if hours > 24:
    print("invalid hours")