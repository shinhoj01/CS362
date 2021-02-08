# Calculate average of list
def find_average(inp):
    try:
        # Change the input to float
        for i in range(0, len(inp)):
            inp[i] = float(inp[i])
        # Finding the average of input
        avg = sum(inp) / len(inp)
        return avg

    # Something wrong with value
    except ValueError:
        return False

    # Divide by zero
    except ZeroDivisionError:
        return False

    # Something wrong with type
    except TypeError:
        return False

if __name__ == "__main__":
    lst = []

    print("Type enter to stop appending element")

    while True:
        inp = input("Enter element: ")
        if (inp != ""):
            lst.append(inp)
        else:
            break
    
    avg = find_average(lst)

    if (avg):
        print("The average of list is {}".format(avg))
    else:
        print("Invalid input")