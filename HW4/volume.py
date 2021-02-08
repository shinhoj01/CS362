# Calculate volume of cube
# returns -1 if error occurs
def find_volume(inp):
    if (str(inp)[0] == '-'):
        return -1
    else:
        try:
            length = float(inp)
            volume =  length * length * length
            return volume
            
        except ValueError:
            return -1

if __name__ == "__main__":
    v = find_volume(input("Enter a length of cube: "))
    if (v != -1):
        print("The volume of cube is {}".format(v))
    else:
        print("Invalid input")