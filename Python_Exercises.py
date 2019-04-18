# Assignment 1 - Day of the week
"""
day = int(input("Day(0-6)?: "))

if day == 0:
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
else:
    print("Please type a number between 0 and 6.")
"""

# Assignment 2 - Work or Sleep in?
"""
day = int(input("Day(0-6)?: "))

if day == 0:
    print("Sleep in")
elif day == 1:
    print("Go to work")
elif day == 2:
    print("Go to work")
elif day == 3:
    print("Go to work")
elif day == 4:
    print("Go to work")
elif day == 5:
    print("Go to work")
elif day == 6:
    print("Sleep in")
else:
    print("Please type a number between 0 and 6.")
"""

#Assignment 3 - Celsius to Fahrenheit
"""
c = int(input("Temperature in Celcius: "))

f = int(c * 1.8 + 32)

print( "%d F" % (f) )
"""


#Assignment 4 - Tip Calculator
"""
bill = int(input("Total bill?: "))
quality = input("How was the service?(good/fair/bad): ")

if quality == "good":
    tip = bill * 0.20
    total = bill + tip
    print("Tip: $ %.2f" % (tip) ) 
    print("Total: $ %.2f" % (total) )
elif quality == "fair":
    tip = bill * 0.15
    total = bill + tip
    print("Tip: $ %.2f" % (tip) )
    print("Total:$ %.2f" % (total) )
else:
    tip = bill * 0.10
    total = bill + tip
    print("Tip: $ %.2f" % (tip) )
    print("Total:$ %.2f" % (total) )
"""
#Assignment 5 - Other Tip Calculator

bill = int(input("Total bill?: "))
quality = input("How was the service?(good/fair/bad): ")
split = int(input("How many way is this bill being split?: "))

if quality == "good":
    tip = bill * 0.20
    total = bill + tip
    per_person = total / split
    print("Tip: $ %.2f" % (tip) ) 
    print("Total: $ %.2f" % (total) )
    print("Amount per person: $ %.2f" % (per_person))
elif quality == "fair":
    tip = bill * 0.15
    total = bill + tip
    per_person = total / split
    print("Tip: $ %.2f" % (tip) )
    print("Total:$ %.2f" % (total) )
    print("Amount per person: $ %.2f" % (per_person))
else:
    tip = bill * 0.10
    total = bill + tip
    per_person = total / split
    print("Tip: $ %.2f" % (tip) )
    print("Total:$ %.2f" % (total) )
    print("Amount per person: $ %.2f" % (per_person))
