#%%
def volume(length):
    # Check if input is numeric
    if (length.isnumeric()):
        # Convert input to integer
        length = int(length)
        volume =  length * length * length
        print("The volume of cube is {} unit^3".format(volume))
    else:
        print("{} is not valid input".format(length))

length = input("Enter a length: ")
volume(length)
input("Press Enter to exit...")



# %%
