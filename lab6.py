# Ryan Willson

def encode(password):
    string = ""  # establishes blank string
    for i, val in enumerate(password):  # allows focus on one character per loop
        val = int(val)
        val += 3  # adds 3 to each integer value
        if (val - 10) >= 0:  # should value equal or exceed 10, 10 is subtracted.
            val -= 10
        string += str(val)  # concatenates string values
    return string

if __name__ == "__main__":
    menu = True
    while menu == True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        print(f"Please enter an option:")
        choice = int(input())  # input establishes desired menu option
        if choice == 1:
            print("Please enter your password to encode:")
            encode(input())  # runs encode function with input
            print("Your password has been encoded and stored!")
        if choice == 2:
            pass
        if choice == 3:
            menu = False  # breaks loop

