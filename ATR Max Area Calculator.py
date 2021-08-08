import math

def another():
    b = input("Would you like to do another? (\"y\" for yes, \"n\" for no) ")
    if b == "n":
        print("Goodbye")
        return False

def check_input_number(input):
    try:
        # Convert it into float
        float(input)
        return True
    except ValueError:
        return False


def coverage():
    while True:
        user_input = input("Enter the Height of ATR7000 from the Ground: ")
        if check_input_number(user_input):
            print("Valid input.")
            height = float(user_input)**2
            area = math.sqrt(3)/2 * 4 * math.tan(math.radians(60))**2 * height
            radius = math.sqrt(area/math.pi)
            diamter = radius * 2
            print()
            print(f"Max ATR Coverage Area = {area:.2f}")
            print(f"Radius at Ground Level = {radius:.2f}")
            print(f"Diameter at Ground Level = {diamter:.2f}")
            break
        else:
            print("Error: Invalid input.")


 


#Main Program Code
while True:
    print("\n==============================================================")
    coverage()
    if not another():
        break

   

"""
import math
import time
a = 1
while a > 0:
    print()
    print('==============================================================')
    h = float(input('Enter the Height of ATR7000 from the Ground: '))**2
    area = math.sqrt(3)/2 * 4 * math.tan(math.radians(60))**2 * h
    #area = 10.4 * h
    r = math.sqrt(area/math.pi)
    d = r * 2
    print()
    print('Max ATR Coverage Area =',(area:.2f))
    print('Radius at Ground Level =',r)
    print('Diameter at Ground Level =',d)
    print()
    print()
    b = input("Would you like to do another? ('y' for yes, 'n' for no) ")
    if b == 'n':
        print("Goodbye")
        time.sleep(1)
        a = 0

"""
