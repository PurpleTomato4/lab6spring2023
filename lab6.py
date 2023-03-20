# Ryan Willson

def encode(password):
    string = ""
    for i, val in enumerate(password):
        val = int(val)
        val += 3
        string += str(val)
    return string

if __name__ == "__main__":

    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    print(f"Please enter an option:")
    choice = int(input())
    menu = True
    while menu == True:
        if choice == 1:
            print("Please enter your password to encode:")
            encode(input())
            print("Your password has been encoded and stored!")
        if choice == 2:
            pass
        if choice == 3:
            menu = False
