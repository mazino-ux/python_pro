
userInp = str(input("Enter a string of words: "))
print("You typed in:", userInp)
currentInp = [userInp]

modInp = str(input("Would you love to make changes to your typed in value, Y or N: ").strip().upper())

while True:
    if modInp == 'Y':
        u = 'Change Values to Uppercase'
        l = 'Change Values to Lowercase'
        c = 'Change all occurrences of a character'
        r = 'Reverse the words'
        z = 'Undo'
        x = 'Exit Game'

        print(f'\n U - {u}\n L - {l}\n R - {r}\n C- {c}\n Z - {z}\n X - {x}\n')

        print('Current Input: ', userInp)
        option = input("Choose from the options above: ").strip().upper()

        if option == 'U':
            userInp = userInp.upper()
            currentInp.append(userInp)
            print('Current change to UpperCase:', userInp)
        elif option == 'L':
            userInp = userInp.lower()
            currentInp.append(userInp)
            print('Current change to LowerCase:', userInp)
        elif option == 'R':
            userInp = userInp[::-1]
            currentInp.append(userInp)
            print('Current change in Reverse:', userInp)
        elif option == 'C':
            ch1 = str(input("Enter the character to replace: ")).casefold()
            ch2 = str(input("Enter the new character: ")).casefold()
            userInp = userInp.replace(ch1, ch2)  
            currentInp.append(userInp)
            print(f'Current change after replacing {ch1} with {ch2}: ', userInp)
        elif option == 'Z':
            if len(currentInp) > 1:
                currentInp.pop()
                userInp = currentInp[-1]
                print('Undo changes:', userInp)
            else:
                print("No more changes to undo.")
        elif option == 'X':
            print('Exiting Application...')
            print('Application Ended...')
            break
        else:
            print('Option not found, select an option from the above listing')
    else:
        break

