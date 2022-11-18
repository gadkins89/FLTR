#Enter the store number and output the number and type of filters
#used for that location.


def title_welcome():
    print("""
***********************************
************* F.L.T.R. ************
***********************************
**Filter Location Tracking Record**
***********************************
********** Version 1.0.0 **********
***********************************
\n""")
    input("Welcome! Please press any key to continue. \n")
    return


def location_selection():
    while True:

        location_number = (input("Please enter a location number: \n"))

        if location_number in asap_location_numbers:
            print(f"You entered location number: {location_number}. Is this correct? \n")
            location_confirmation = input("(Y/N) ").lower()
            if location_confirmation == "y":
                break
            elif location_confirmation =="n":
                print(" Let us try this again.. \n")
            else:
                print(f"{location_confirmation} is an invalid selection. Please try again. \n")
        else:
            print(f"{location_number} is an invalid location number. Please try again. \n")
    return location_number


def filters_used(location_filter_dict):
    print("The filters used for this location are: \n")
    print("Filters:        Qty: \n")
    for k, v in dict.items(location_filter_dict):
        print(f"{k} {v:^11}")
    return


asap_location_numbers = ["101", "102", "103", "104", "300", "301", "302", "304", "305", "307", "308", "310", "311", "313", "322", "330", "332", "000"]

asap_101_filters = {"1in 1qt Gas": 2, "1in 2qt Gas": 10, "1in 2qt Dsl": 2, "1.5in HiFlo": 12}
asap_102_filters = {"1in 1qt Dsl": 1, "1in 2qt Gas": 12, "1in 2qt Dsl": 3}
asap_103_filters = {"1in 2qt Gas": 12, "1in 2qt Dsl": 4}
asap_104_filters = {"1in 1qt Gas": 1, "1in 1qt Dsl": 1, "1in 2qt Gas": 11, "1in 2qt Dsl": 3, "1.5in HiFlo": 6}
asap_300_filters = {"1in 2qt Gas": 6, "1in 2qt Dsl": 1, "1.5in HiFlo": 6}
asap_301_filters = {"1in 2qt Gas": 4, "1.5in HiFlo": 5}
asap_302_filters = {"1in 1qt Gas": 7, "1.5in HiFlo": 12}
asap_304_filters = {"1in 1qt Gas": 3, "1in 2qt Gas": 2, "1.5in HiFlo": 8}
asap_305_filters = {"1in 2qt Gas": 4, "1in 2qt Dsl": 1}
asap_307_filters = {"1in 2qt Gas": 18, "1in 2qt Dsl": 8}
asap_308_filters = {"1in 1qt Gas": 12, "1in 1qt Dsl": 4, "1.5in HiFlo": 3}
asap_310_filters = {"1in 2qt Gas": 8, "1in 2qt Dsl": 4}
asap_311_filters = {"1in 2qt Gas": 24, "1in 2qt Dsl": 8}
asap_313_filters = {"1in 1qt Gas": 12, "1in 2qt Dsl": 4, "1.5in HiFlo": 10}
asap_322_filters = {"1in 1qt Gas": 00, "1in 2qt Gas": 00, "1in 2qt Dsl": 00, "1.5in HiFlo": 00}
asap_330_filters = {"1in 2qt Gas": 13, "1in 2qt Dsl": 4, "1.5in HiFlo": 8}
asap_332_filters = {"1in 1qt Gas": 15, "1in 1qt Dsl": 5, "1.5in HiFlo": 14}
hydro_filters = {"1in 2qt Gas": 4, "1.5in HiFlo": 4}


title_welcome()


while True:


    location_number = location_selection()

    if location_number == "101":
        filters_used(asap_101_filters)
    elif location_number == "102":
        filters_used(asap_102_filters)
    elif location_number == "103":
        filters_used(asap_103_filters)
    elif location_number == "104":
        filters_used(asap_104_filters)
    elif location_number == "300":
        filters_used(asap_300_filters)
    elif location_number == "301":
        filters_used(asap_301_filters)
    elif location_number == "302":
        filters_used(asap_302_filters)
    elif location_number == "304":
        filters_used(asap_304_filters)
    elif location_number == "305":
        filters_used(asap_305_filters)
    elif location_number == "307":
        filters_used(asap_307_filters)
    elif location_number == "308":
        filters_used(asap_308_filters)
    elif location_number == "310":
        filters_used(asap_310_filters)
    elif location_number == "311":
        filters_used(asap_311_filters)
    elif location_number == "313":
        filters_used(asap_313_filters)
    elif location_number == "322":
        filters_used(asap_322_filters)
    elif location_number == "330":
        filters_used(asap_330_filters)
    elif location_number == "332":
        filters_used(asap_332_filters)
    elif location_number == "000":
        filters_used(hydro_filters)

    change_location = input("Would you like to search a different location? (Y/N) \n").lower()

    if change_location == "y":
        continue
    else:
        input("Thank you for using F.L.T.R.! Press any key to exit. \n")
        exit
        break