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


def calculate(height_atr, height_tag, scan_angle, scan_angle_use):
    if check_input_number(scan_angle, 0, 60):
        height_atr = float(height_atr)
        height_tag = float(height_tag)
        height_max_accuracy = height_atr - height_tag
        
        circle_radius = math.tan(math.radians(scan_angle)) * height_atr
        spacing = 2 * circle_radius #This is also equal to the circle diameter
        circle_area = math.pi * circle_radius**2
        
        hex_cell_area = math.sqrt(3)/2 * spacing**2
        
        
        area = (math.sqrt(3)/2) * (4*(math.tan(math.radians(scan_angle))**2)) * (height_atr**2)
        radius = math.sqrt(area/math.pi)
        diamter = radius * 2

        print(f"\nAt a height of {height_atr:.2f} and a {scan_angle_use} elevation scan angle of {scan_angle:.2f} degrees, at ground level the:")
        print(f"\n\tMax ATR Coverage Area = {area:.2f}")
        print(f"\tRadius of the Circle Coverage Area = {circle_radius:.2f}")
        print(f"\tDiameter of the Circle Coverage Area = {spacing:.2f}")
        print(f"\nAdditionally, the spacing between each ATR = {spacing:.2f}")
        print(f"\tHexagional cell area = {hex_cell_area:.2f}")
    else: 
        print("\nError: Invalid scan angle.")

def check_input_number(input, minimum, maximum):
    try:
        # Try to convert it to float & test it is greater then 0.
        return float(input) >= float(minimum) and float(input) <= float(maximum)
    except ValueError:
        return False


def coverage(som):
    while True:
        user_input_height_atr = input("\nEnter the Height of ATR7000 from the Ground: ")
        if check_input_number(user_input_height_atr, som[2], som[3]):
            while True:
                user_input_height_tag = input("\nEnter the Maximum Tag Height: ")
                if check_input_number(user_input_height_tag, 0, user_input_height_atr):                
                    # calculate(user_input_height_atr, 60, "default")
                    # calculate(user_input_height_atr, 54.7, "recommended location accuracy")
                    break # Break tag input loop
                else:
                    print(f"\nError: Invalid Tag height. Accepted values are between 0.00 and {user_input_height_atr} {som[1]} inclusive.")
            break # Break ATR input loop
        else:
            print(f"\nError: Invalid ATR height. Accepted values are between {som[2]:.2f} and {som[3]:.2f} {som[1]} inclusive.")


def set_SoM():
    while True:
        user_input = input("\nAre you using the Metric system? (\"y\" or \"n\") ")
        if user_input.lower() == "y":
            return ["Metric", "metres", 3.6576, 6.0960]
        elif user_input.lower() == "n":            
            return ["Imperial", "feet", 12, 20]
        else:
            print("\nError: Invalid input.")


# Main Program Function
def main():
    print("\n==============================================================")
    som = set_SoM() # som is a list, containing the System of Measurement (SoM), Unit of Measurement (UoM), UoM Minimum Value, and UoM Maximum Value.
    # print(f"\nSystem of Measurment = {som[0]} {som[1]} {som[2]} som[3]}")
    print(f"\nPlease enter all height measurements in {som[1]}.")
    while True:
        print("\n==============================================================")
        coverage(som)
        if another() == False :
            break


# Check if program is being called explicitly
if __name__ == "__main__":
  main()