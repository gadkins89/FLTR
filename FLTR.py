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

asap_101_filters = {"1in 1qt Gas": 2, "1in 2qt Gas": 10, "1in 2qt Diesel": 2, "1.5in High Flow": 12}
asap_102_filters = {"1in 1qt Diesel": 1, "1in 2qt Gas": 12, "1in 2qt Diesel": 3}


def filters_at_location(location_number):
    print("The filters used for this location are: \n")
    for k, v in dict.items(location_number):
        print(k, v) 



welcome_message = input("Welcome! Please press any key to continue. \n")

while True:

    location_number = int(input("Please enter a location number: \n"))

    if location_number in asap_location_numbers:
        print(f"You entered location number: {location_number}. Is this correct? \n")
        location_confirmation = input("(Y/N) ").lower()
        if location_confirmation == "y":
            break
        else:
            print(" Let us try this again.. \n")
    else:
        print(f"{location_number} is not a valid location number. Please try again. \n")

if location_number == 101:
   filters_at_location(asap_101_filters)
elif location_number == 102:
    filters_at_location(asap_102_filters)
    

