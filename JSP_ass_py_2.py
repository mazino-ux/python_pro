
userInp = input("Enter a string of words: ")
print("You typed in:", userInp)
currentInp = [userInp]

u = 'Change Values to Uppercase'
l = 'Change Values to Lowercase'
c = 'Change all occurrences of a character'
r = 'Reverse the words'
z = 'Undo'
x = 'Exit Game'

print(f'\n U - {u}\n L - {l}\n R - {r}\n C- {c}\n Z - {z}\n X - {x}\n')

while True:
    option = input().strip().upper()

    if option == 'U':
        userInp = userInp.upper()
        currentInp.append(userInp.casefold())
    elif option == 'L':
        userInp = userInp.lower()
        currentInp.append(userInp)
    elif option == 'R':
        userInp = userInp[::-1]
        currentInp.append(userInp)
    elif option == 'C':
        ch1 = input().casefold()
        ch2 = input().casefold()
        userInp = userInp.replace(ch1, ch2)
        currentInp.append(userInp)
    elif option == 'Z':
        if len(currentInp) > 1:
            currentInp.pop()
            userInp = currentInp[-1].casefold()
        else:
            print("No more changes to undo.")
    elif option == 'X':
        print(userInp)
        break














