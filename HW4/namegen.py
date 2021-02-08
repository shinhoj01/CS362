def generate(first, last):
    if (first.isalpha() and last.isalpha()):
        full = first + " " + last
        return full
    else:
        return False

if __name__ == "__main__":
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    full = generate(first, last)
    if (full):
        print(full)
    else:
        print("Invalid input")