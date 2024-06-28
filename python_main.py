
#  ------------------------------ && •SORTING• && ----------------------------
# def my_func(n):
#     return abs(n - 95)
# this_list = [100, 50, 65, 82, 24]
# this_list.sort(key=my_func)
# print(this_list)
# my_array = [64, 34, 25, 12, 22, 11, 90, 5]
# n = len(my_array)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if my_array[j] > my_array[j+1]:
#             my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
#
# print(my_array)
# ------------------------------ && •BUBBLE SORTING• && ----------------------------
# my_x = [500, 76, 89, 95, 455, 34, 10]
# a = len(my_x)
# for x in range(a - 1):
#     swapped = False
#     for b in range(a - x - 1):
#         if my_x[b] > my_x[b + 1]:
#             my_x[b], my_x[b + 1] = my_x[b + 1], my_x[b]
#             swapped = True
#     if not swapped:
#         break
# print("Ans is: ", my_x)
#
# print()
# print("Simple sorting:", sorted(my_x))
# my_x.sort(reverse=True)
# print(my_x)

# humans = {"Name": "Mathena", "Age": "19", "YOB": 2007, "DOB": 6, "MOB": 4, "Religion": "Christianity"}
# print(humans)
# print()
#
# new_humans = humans.copy()
# humans.update({"DOB": {"DD": 6, "MM": 4, "YY": 2007}})
# humans.pop("YOB")
# humans.pop("MOB")
# for i in new_humans.items():
#     print(i)
# print()
# print(humans)
#
# import statistics
# import numpy
# speed = [20, 30, 40, 10, 15, 10, 30, 50, 85, 75, 46, 74, 89, 31, 10, 25, 23]
# x = numpy.median(speed)
# print(x)
# median = statistics.median(speed)
# print("Median is:", median)
# print()
#
# speed.sort()
# n = len(speed)
# if n % 2 == 0:
#     mid_no = (speed[n // 2 - 1])
# else:
#     mid_no = (speed[n // 2])
# print("Middle No is: ", mid_no)
#
# #
# a = 5
# print("I am " + str(a) + " years old")

# a = b = 34
#
# print(a)

# a = 3
# for i in range(1, 13):
#     x = a * i
#     print(a, " * " , i , " = " , x)

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

#
# Trinity is God's Little Princess
#
#
#
