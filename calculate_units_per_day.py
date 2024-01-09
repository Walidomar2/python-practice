hours_in_day = 24
min_in_day = 24*60
sec_in_day = 24*60*60


def calculate_hours(number_of_days, unit):
    capUnit = unit.capitalize()
    print(capUnit)

    if capUnit == "Hours":
        return f"{number_of_days} days = {number_of_days * hours_in_day} {capUnit}"
    elif capUnit == "Minuts":
        return f"{number_of_days} days = {number_of_days * min_in_day} {capUnit}"
    elif capUnit == "Seconds":
        return f"{number_of_days} days = {number_of_days * sec_in_day} {capUnit}"
    else:
        return "Please Enter a valid unit: (Hours, Minuts, Seconds)"


def validate_and_execute():
   # if user_input.isdigit():
    try:
        int_user_input = int(days_unit_dict["days"])
        if int_user_input > 0:
            return calculate_hours(int_user_input, days_unit_dict["units"])
        elif int_user_input <= 0:
            return "Please enter a number > 0 "
    except ValueError:
        return "please enter a valid number"


user_input = ""

while user_input != "exit":
    user_input = input(
        "Enter a list of days:unit with comma separated: ")  #EX==> 40:hours, 30:minuts, 20:seconds

    for element in user_input.split(", "):
        # print(num_of_days)
        days_unit_element = element.split(":")
        days_unit_dict = {
            "days": days_unit_element[0], "units": days_unit_element[1]}
        print(validate_and_execute())
