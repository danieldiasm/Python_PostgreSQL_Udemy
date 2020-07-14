# Remember that every input returns string ALWAYS
the_input = input("How big is you mama (in quare feet): ")
square_feet = int(the_input)
square_meters = square_feet / 10.8
# Always convert before making any math.
print(f"Your mama in {square_feet} sqf, measures up {square_meters:.2f} in square meters.")
# :.2f rounds up the decimal spaces for only two digits places.