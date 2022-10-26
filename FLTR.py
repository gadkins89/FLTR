"""
Enter the store number and output the number and type of filters
used for that location.
"""

print("""
***********************************
************* F.L.T.R. ************
***********************************
**Filter Location Tracking Record**
***********************************
********** Version 1.0.0 **********
***********************************
""")

asap_location_numbers = [101, 102, 103, 104, 300, 301, 302, 304, 305, 307, 308, 310, 311, 313, 322, 330, 332]

asap_101 = {"filters": "(12) ==> 1in 2qt Gas (4) ==> 1in 2qt Auto Diesel (12) ==> 1.25in 3qt High Flow"}

welcome_message = input("Welcome! Please press any key to continue. \n")

while True:

    location_number = int(input("Please enter a location number: \n"))

    if location_number in asap_location_numbers:
        print(f"You entered location number: {location_number}. Is this correct? \n")
        location_confirmation = input("(y/n) ")
        if location_confirmation == "y":
            break
        else:
            print(" Let us try this again.. \n")
    else:
        print(f"{location_number} is not a valid location number. Please try again. \n")

if location_number == 101:
    print("The filters used for this location are: \n")
    print(asap_101["filters"])
    

