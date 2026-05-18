# Weight conversion program, kilo to pounds and vice versa!


answer = input(
    "Enter either Kg or lbs, to know how much your input is in the other weight type: "
)

if answer == "kg" or answer == "KG" or answer == "kilogram":

    def kg_to_lbs_weight_converter(number):
        return number * 2.20462

    fax = float(input("Enter weight amount: "))
    print(kg_to_lbs_weight_converter(fax))
elif answer == "lbs" or answer == "pounds" or answer == "LBS":

    def lbs_to_kg_weight_converter(number):
        return number * 0.4536

    gilbert = float(input("Enter weight amount: "))
    print(lbs_to_kg_weight_converter(gilbert))
else:
    print("Wrong input!")
