# Calculate volume
def volume(inp):
    try:
        length = float(inp)
        volume =  length * length * length
        return volume
        
    except ValueError:
        print("Invalid input")

v = volume(input("Enter a length of cube: "))

if(isinstance(v, float)):
    print("The volume of cube is {} unit^3".format(v))

# %%