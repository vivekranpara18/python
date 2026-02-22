import converter 

#take input 
meter = float(input("enter value in meter :"))
foot = float(input("enter value in foot :"))
cm = float(input("enter value in centimeters :"))

inch = converter.meter_to_inch(meter)
print(f"{inch} of {meter} meter")

inch = converter.foot_to_inch(foot)
print(f"{inch} of {foot} foot")

inch = converter.cm_to_inch(cm)
print(f"{inch} of {cm} centimeter")