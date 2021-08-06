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
