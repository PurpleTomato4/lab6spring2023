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

def decoder(store):
    string = list(store)
    for i, val in enumerate(store):  # allows focus on one character per loop
        if int(string[i]) >= 3: # should value equal of be greater than 3, subtract 3
            string[i] = str(int(string[i]) - 3)
        else:
            diff = 10 - int(string[i])
            string[i] = str(diff+1)
    string = ''.join(string)
    return string


if __name__ == "__main__":
    menu = True
    while menu == True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        print(f"Please enter an option:")
        choice = int(input())  # input establishes desired menu option
        if choice == 1:
            print("Please enter your password to encode:")
            store = encode(input())  # runs encode function with input
            print("Your password has been encoded and stored!\n")
        if choice == 2:
            decoded = decoder(store)
            print(f'The encoded password is {store}, and the original password is {decoded}.')
        if choice == 3:
            menu = False  # breaks loop

