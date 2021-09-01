import math

def another():
    while True:
        user_input = input("\nWould you like complete another coverage calculation? (\"y\" or \"n\"): ")
        if user_input.lower() == "y":
            return True
        elif user_input.lower() == "n":            
            print("\nThank you and goodbye!")
            return False
        else:
            print("\nError: Invalid input.")


def calculate_coverage(height_atr, height_tag):
    height_atr = float(height_atr)
    height_tag = float(height_tag)
    height_max_accuracy = height_atr - height_tag
    
    # Radius calculation validated using https://www.omnicalculator.com/math/triangle-30-60-90
    default_circle_radius = math.tan(math.radians(60)) * height_atr
    default_spacing = 2 * default_circle_radius #This is also equal to the default circle diameter
    default_circle_area = math.pi * default_circle_radius**2
    
    default_hex_cell_area = math.sqrt(3)/2 * default_spacing**2

    typical_circle_radius = math.tan(math.radians(54.7)) * height_max_accuracy
    typical_spacing = 2 * typical_circle_radius #This is also equal to the typical circle diameter
    typical_circle_area = math.pi * typical_circle_radius**2

    typical_hex_cell_area = math.sqrt(3)/2 * typical_spacing**2

    max_accuracy_spacing = 0.85 * typical_spacing
    max_accuracy_hex_cell_area = math.sqrt(3)/2 * max_accuracy_spacing**2
    
    # Build a dictionary that will be returned and contains all the calculated values
    results = {
        "height_atr" : height_atr,
        "height_tag" : height_tag,
        "height_max_accuracy" : height_max_accuracy,
        "default_circle_radius" : default_circle_radius,
        "default_spacing": default_spacing,
        "default_circle_area" : default_circle_area,
        "default_hex_cell_area" : default_hex_cell_area,
        "typical_circle_radius" : typical_circle_radius,
        "typical_spacing" : typical_spacing,
        "typical_circle_area" : typical_circle_area,
        "typical_hex_cell_area" : typical_hex_cell_area,
        "max_accuracy_spacing" : max_accuracy_spacing,
        "max_accuracy_hex_cell_area" : max_accuracy_hex_cell_area
    }

    return results


def check_input_number(input, minimum, maximum):
    try:
        # Try to convert it to float & test it is within the accepted range.
        return float(input) >= float(minimum) and float(input) <= float(maximum)
    except ValueError:
        return False


def coverage(som):
    while True:
        user_input_height_atr = input("\nEnter the Height of ATR7000 from the Ground: ")
        if check_input_number(user_input_height_atr, som[2], som[3]):
            while True:
                user_input_height_tag = input("\nEnter the Maximum or Average Tag Height: ")
                if check_input_number(user_input_height_tag, 0, user_input_height_atr):                
                    results = calculate_coverage(user_input_height_atr, user_input_height_tag)

                    # Print out the default results
                    description = f"Default"
                    printout_coverage(description, som[1], 60, results["height_atr"], 0, results["default_hex_cell_area"], results["default_spacing"], results["default_circle_radius"], results["default_spacing"], results["default_circle_area"])

                    # Print out the typical results
                    description = f"Typical"
                    printout_coverage(description, som[1], 54.7, results["height_atr"], results["height_tag"], results["typical_hex_cell_area"], results["typical_spacing"], results["typical_circle_radius"], results["typical_spacing"], results["typical_circle_area"])

                    # Print out the max results
                    description = f"Maximum Accuracy"
                    notes = "Please note, to achieve maximum accuracy, spacing has been reduced by 15%."
                    printout_coverage(description, som[1], 54.7, results["height_atr"], results["height_tag"], results["max_accuracy_hex_cell_area"], results["max_accuracy_spacing"], results["typical_circle_radius"], results["typical_spacing"], results["typical_circle_area"], notes)

                    break # Break tag height input loop
                else:
                    print(f"\nError: Invalid Tag height. Accepted values are between 0.00 and {user_input_height_atr} {som[1]} inclusive.")
            break # Break ATR height input loop
        else:
            print(f"\nError: Invalid ATR height. Accepted values are between {som[2]:.2f} and {som[3]:.2f} {som[1]} inclusive.")


def printout_coverage(description, uom, scan_angle, height_atr, height_tag, hex_cell_area, spacing, circle_radius, circle_diametre, circle_area, notes = ""):
    print(f"\n\n{description} Coverage Area:")
    
    print(f"\n\tATR mount height = {height_atr:.2f} {uom}")
    print(f"\tElevation scan angle = {scan_angle}\N{DEGREE SIGN}")
    print(f"\tMaximum/Average Tag Height = {height_tag:.2f} {uom}")
    
    print(f"\n\tATR Hexagonal Coverage Area = {hex_cell_area:.2f} {uom}\N{SUPERSCRIPT TWO}")
    print(f"\tThe spacing between each ATR = {spacing:.2f} {uom}")
    
    if notes != "":
        print(f"\t\t{notes}")
    
    print(f"\n\tAs an FYI, Circle Coverage:")
    print(f"\n\t\tRadius = {circle_radius:.2f} {uom}")
    print(f"\t\tDiameter = {circle_diametre:.2f} {uom}")
    print(f"\t\tArea = {circle_area:.2f} {uom}\N{SUPERSCRIPT TWO}")


def set_SoM():
    while True:
        user_input = input("\nAre you using the Metric system? (\"y\" or \"n\"): ")
        if user_input.lower() == "y":
            return ["Metric", "metres", 3.6576, 6.0960]
        elif user_input.lower() == "n":            
            return ["Imperial", "feet", 12.00, 20.00]
        else:
            print("\nError: Invalid input.")


# Main Program Function
def main():
    print("\n==============================================================")
    print("\n            Welcome to the ATR Coverage Calculator")
    # som is a list, containing the System of Measurement (SoM), Unit of Measurement (UoM), UoM Minimum Value, and UoM Maximum Value.
    som = set_SoM()
    print(f"\nPlease note, {som[0]} system requires height measurements in {som[1]}.")
    print("\n            **************************************")
    while True:
        coverage(som)
        print("\n            **************************************")
        if another() == False :
            break


# Check if program is being called explicitly
if __name__ == "__main__":
  main()