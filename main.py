data = []

while True:
    # Ask for name and height
    name = input("What is the person's name?\n").title()
    height_input = input("What is the person's height in meters?\n")

    try:
        # Try to convert the height to float. If input is not a number, raise ValueError.
        height = float(height_input)
    except ValueError:
        print("Input is not a number. Restart the program.")
        continue

    if height > 2.4:
        # If height is more than 2.4, restart the program
        print("Height is not correct. Restart the program.\n")
        continue

    weight_input = input("How much does the person weigh in kilograms?\n")

    try:
        # Try to convert the weight to float. If input is not a number, raise ValueError.
        weight = float(weight_input)
    except ValueError:
        print("Input is not a number. Restart the program.")
        continue

    # Creates a list of dictionaries of all the data input by the user
    data.append({"name": name, "height": height, "weight": weight})

    # Asks the user if they want to keep going
    going = input("Keep going?\nType 'no' to stop.\n").lower()
    if going == "no" or going == "n":
        break

new_list = []

for person in data:
    # Calculates BMI value
    result = person["weight"] / (person["height"] ** 2)
    name = person["name"]

    if result < 18.5:
        bmi = "Underweight"
    elif result < 24.9:
        bmi = "Normal Healthy Weight"
    elif result < 29.9:
        bmi = "Overweight"
    elif result < 39.9:
        bmi = "Obese"
    else:
        bmi = "Morbidly Obese"

    # Creates a new list of people's names and BMI category classification
    new_list.append({"name": name, "bmi": bmi})

for person in new_list:
    # Prints out people's names and BMI category classification
    print(f"{person['name'].title()} is {person['bmi']}")