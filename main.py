# Paola Bechalani
def encoder(password):
    pw_return = ""
    value = 0
    for i in range(len(password)):
        value = int(password[i]) + 3
        pw_return += str(value)
    return pw_return




    

# Daphne Calin
def decoder(password):
    pw_return = ""
    value = 0
    for i in range(len(password)):
        value = int(password[i]) - 3
        pw_return += str(value)
    return pw_return


def main():
    option = ""
    pw = ''
    while option != "3":
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = input("Please enter an option:")

        if option == "1":
            pw = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            pw = encoder(pw)
        elif option == "2":
            print(f'The encoded password is {pw}, and the original password is {decoder(pw)}.')  # needs decoder function to be implemented
        elif option == "3":
            break


if __name__ == "__main__":
    main()