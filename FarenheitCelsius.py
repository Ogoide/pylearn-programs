
repeat = True

while repeat:
    tbc = input("Farenheit or Celsius? (F or C)\nPress 'E' to exit.\n").capitalize()
    if tbc == "F":
        try:
            temp = float(input("Enter the temperature\t"))
            c = (5 / 9) * (temp - 32)
            print(f"The temperature is {c:.2f}ºC.")
        except:
            print("Enter a valid float type value.\nRESTARTING PROGRAM...\n")
    elif tbc == "C":
        try:
            temp = float(input("Enter the temperature\t"))
            f = ((9 / 5) * temp) + 32
            print(f"The temperature is {f:.2f}F.")
        except:
            print("Enter a valid float type value.\nRESTARTING PROGRAM...\n")
    elif tbc == "E":
        print("PROGRAM EXITED")
        repeat = False

    else:
        print("F or C?\nRESTARTING PROGRAM...\n")
