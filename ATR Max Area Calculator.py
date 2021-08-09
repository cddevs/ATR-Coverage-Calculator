import math

def another():
    while True:
        user_input = input("\nWould you like complete another coverage calculation? (\"y\" or \"n\") ")
        if user_input.lower() == "y":
            return True
        elif user_input.lower() == "n":            
            print("\nThank you and goodbye!")
            return False
        else:
            print("\nError: Invalid input.")


def calculate_coverage_area(height, scan_angle, scan_angle_use):
    if check_input_number(scan_angle):  
        height = float(height)
        area = (math.sqrt(3)/2) * (4*(math.tan(math.radians(scan_angle))**2)) * (height**2)
        radius = math.sqrt(area/math.pi)
        diamter = radius * 2
        print(f"\nAt a height of {height:.2f} and a {scan_angle_use} elevation scan angle of {scan_angle:.2f} degrees, at ground level the:")
        print(f"\n\tMax ATR Coverage Area = {area:.2f}")
        print(f"\tRadius of the Coverage Area = {radius:.2f}")
        print(f"\tDiameter of the Coverage Area = {diamter:.2f}")
    else:
        print("\nError: Invalid scan angle.")


def check_input_number(input):
    try:
        # Try to convert it to float & test it is greater then 0.
        return float(input) > 0
    except ValueError:
        return False


def coverage():
    while True:
        user_input = input("\nEnter the Height of ATR7000 from the Ground: ")
        if check_input_number(user_input):
            calculate_coverage_area(user_input, 60, "default")
            calculate_coverage_area(user_input, 54.7, "recommended location accuracy")
            break
        else:
            print("\nError: Invalid height input.")


#Main Program Code
while True:
    print("\n==============================================================")
    coverage()
    if another() == False :
        break