__author__ = "Luis Martinez"

# uses imported math to make more complex calculations
import math  # Imports math to be used


def menu():
    """
prints a menu to choose from
    """
    print("Menu")
    print('1.Calculate the Volume of a Sphere')
    print('2.Calculate the Circumference of a Circle')
    print('3.Show Evens and their square roots between 40 down to 30')
    print('4.Calculate Balance in Savings Account After Every Three Months')
    print('5.View country statistics')
    print('6.Play with numbers')
    print('7.Quit')


def radius():
    """
defines radius by asking for input and checking for validity of input
    :return:
    """
    global r
    moveOn = True
    while moveOn:
        # Asks for an input
        r2 = input('Input radius of sphere:')
        # The input then goes through checks to verify a valid input
        try:
            # The input is checked to see if it is a number
            # In this case it can be a floating point number
            r = float(r2)
            if r > 0:
                # If the number is a valid number and it is greater than 0 then
                # the value is returned
                moveOn = False
            else:
                # If the number is not a positive number then it will print the
                # following
                print("Please enter a positive number for radius")
                # It will then ask the user for another input until a valid one
                # can be returned

        # It accepts the value error for anything other than a number being the
        # input
        except ValueError:
            # It will then print the following
            print("Please enter a valid number!")
            # The user will then be asked for another input until a valid one
            # can be returned
    # Returns r to be used
    return r


def volume(r):
    """
uses the parameter r to find the volume of a sphere
    :param r:
    :return:
    """
    # Uses imported math to be able to use pi
    v = 4 / 3 * math.pi * r ** 3  # The equation for the volume of a circle
    # Returns v to be used
    return v


def display1(r, v):
    """
Uses both parameters r and v to format and print output
    :param r:
    :param v:
    """
    print('-------------------------')  # Prints, formats and aligns output
    print('Radius: {0:>15.2f}'.format(r))
    print('Volume: {0:>15.2f}'.format(v))
    print('-------------------------')


def diameter(r):
    """
Uses the parameter r to calculate the diameter of a circle
    :param r:
    :return:
    """
    # Calculates tje diameter of the circle
    d = 2 * r  # Equation for diameter of a circle
    # Returns d to be used
    return d


def circumference(r):
    """
Uses the parameter r to calculate the circumference of a circle
    :param r:
    :return:
    """
    # Calculates the circumference of the circle
    c = 2 * math.pi * r  # The equation for the circumference of a circle
    # Returns c to be used
    return c


def display2(r, d, c):
    """
Uses the parameters r,d, and c to format and print output
    :param r:
    :param d:
    :param c:
    """
    print('-------------------------')  # Prints, formats and aligns output
    print('Radius:       {0:>8.2f}'.format(r))
    print('Diameter:     {0:>8.2f}'.format(d))
    print('Circumference:{0:>8.2f}'.format(c))
    print('-------------------------')


def initialDeposit1():
    """
Defines initialDeposit1 by asking for an input and checking validity of input
    :return:
    """
    global id
    moveOn = True
    while moveOn:
        # Asks user for an input
        initialDeposit = input("Enter amount deposited: ")
        try:
            # The input is checked to see if it is a number
            # In this case it can be a floating point number
            id = float(initialDeposit)
            # Checks to see if the input is a positive number
            if id > 0:
                # If the value is a positive number then it is returned
                moveOn = False
            else:
                # If the value is not a positive number then it prints the
                # following
                print("Please enter a positive number")
        # If anything other than a number is input then it goes here to accept
        # that error
        except ValueError:
            # It then prints the following and asks the used for another input
            # until a valid one can be returned
            print("Enter a number!")
    # Returns id to be used
    return id


def annualRate0fInterest1():
    """
Defines annualRateOfInterest by asking for an input and checking validity of
input
    :return:
    """
    global ar
    moveOn = True
    while moveOn:
        # Asks the user for an input
        annualRate0fInterest = input("Enter annual rate of interest; such as "
                                     ".02, .03, or .04: ")
        try:
            # The input is checked to see if it is a number
            # In this case it can be a floating point number
            ar = float(annualRate0fInterest)
            # Checks to see if the input is a positive number
            if ar > 0:
                # If the value is a positive number then it is returned
                moveOn = False
            else:
                # If the value is not a positive number then it prints the
                # following
                print("Please enter a positive interest rate")
        # If anything other than a number is input then it goes here to accept
        # that error
        except ValueError:
            # It then prints the following and asks the used for another input
            # until a valid one can be returned
            print("Enter a number!")
    # Returns ar to be used
    return ar


def monthlyRate0fInterest(ar):
    """
Uses parameter ar to calculate the monthly rate of interest
    :param ar:
    :return:
    """
    # Gets the monthly rate of interest by dividing the annual rate by 12
    mri = ar / 12
    # Returns mri to be used
    return mri


def display3(id, mri):
    """
Uses parameters id and mri to format and print output
    :param id:
    :param mri:
    """
    # Prints, formats and aligns output
    print('-------------------------')
    print("{0}	{1:>15}".format("Month", "Balance"))
    # This program is for every 3 months so this part calculates every 3 months
    for i in range(3, 13, 3):
        print("{0:2}	       ${1:>8,.2f}".
              format(i, id * (1 + mri) ** i))
    print('-------------------------')


def x1():
    """
Defines x1 by asking for an inout and checking validity of input
    :return:
    """
    global x
    moveOn = True
    while moveOn:
        # Asks user for an input
        x2 = input('Please Make a Selection:')

        try:
            # The input is checked to see if it is a number
            # In this case it has to be an integer
            x = int(x2)
            # Checks to see if the number entered is an option
            if x <= 7 and x > 0:
                # If it is an option then it is returned
                moveOn = False
            # If is is not an option then it prints the following
            else:
                print("Please select a menu option!")
        # If the input is not a number then it goes here
        except ValueError:
            # The following is printed
            print("Please select a menu option!")
            # The user is then asked for another input until a valid one can be
            # returned
    # Returns x to be used
    return x


# Defines menu if option 5 is selected
def menu1():
    """
The menu for if the user selects option 5
    """
    print('Main Menu')
    print('1. Display the Country data that startswith a certain letter')
    print('2. Display countries population<1 million')
    print('3. Display the land area greater than 1,000,000')
    print('4. Quit')


def cletter():
    """
Defines cletter
It opens the UN.txt and asks the user for an input
The input is then capitalized and the program searches the first letter of
each line and if it starts with the letter then it is printed
    """
    # Opens the file UN.txt to be used
    infile = open('UN.txt', 'r')
    # Asks the user for an input
    letter = input("Enter the first letter of a country: ")
    # Ensures the letter is an uppercase letter
    letter = letter.upper()
    print('-------------------------------------------------------------------'
          '-----')
    # Formats header
    print('{0:42}{1:21}{2:10}'.format('Country', 'Population', 'Land Area'))
    print('-------------------------------------------------------------------'
          '-----')
    # Extracts data from file only if it begins with the letter input
    for x in infile:
        # Splits the data up by commas
        data = x.split(',')
        # Position 0 is the country name
        country = data[0]
        # Position 2 is the population
        # Population is by the million so to show that it multiplies the value
        # by a million
        pop = 1000000 * eval(data[2])
        # Position 3 is the land area
        area = eval(data[3])
        # If the country starts with the letter input then it will print its
        # data and format it
        if x.startswith(letter):
            print('{0:41}{1:12,.1f}{2:19,}'.format(country, pop, area))
    print('-------------------------------------------------------------------'
          '-----')
    # Closes the file
    infile.close()


def pop():
    """
Defines pop by opening the UN.txt file and reading its contents
It splits the data up by the commas and by doing so is able to look at specific
elements on each line
In this case it is looking at the first value and the third value (Represented
by data[0] and data[2])
data[2] is searched and if it meets the criteria it is printed along with
data[0]
    """
    infile = open('UN.txt', 'r')
    print('-------------------------------------------------------------------'
          '-----')
    print('{0:62}{1:10}'.format('Country', 'Population'))
    print('-------------------------------------------------------------------'
          '-----')
    for x in infile:
        data = x.split(',')
        country = data[0]
        pop = 1000000 * eval(data[2])
        if pop < 1000000:
            print('{0:62}{1:10,}'.format(country, pop))
    print('-------------------------------------------------------------------'
          '-----')
    infile.close()


def area():
    """
Defines area by opening the UN.txt file and reading its contents
It splits the data up by the commas and by doing so is able to look at specific
elements on each line
In this case it is looking at the first value and the third value (Represented
by data[0] and data[3])
data[3] is searched and if it meets the criteria it is printed along with
data[0]
    """
    infile = open('UN.txt', 'r')
    print('-------------------------------------------------------------------'
          '-----')
    print('{0:63}{1:10}'.format('Country', 'Land Area'))
    print('-------------------------------------------------------------------'
          '-----')
    for x in infile:
        data = x.split(',')
        country = data[0]
        area = eval(data[3])
        if area > 1000000:
            print('{0:62}{1:10,}'.format(country, area))
    print('-------------------------------------------------------------------'
          '-----')
    infile.close()


def y1():
    """
Defines the input for y for the second menu
It ensures that a valid number input is inserted
It will keep asking for an input until a valid input is inserted
    :return:
    """
    global y
    moveOn = True
    while moveOn:
        y2 = input('Please Make a Selection:')

        try:
            y = float(y2)
            if y <= 4 and y > 0:
                moveOn = False
            else:
                print("Please select a menu option!")
        except ValueError:
            print("Please select a menu option!")
    return y


x = 8
while x != 7:
    menu()
    x = x1()
    if x == 1:
        r = radius()
        v = volume(r)
        display1(r, v)
    if x == 2:
        r = radius()
        d = diameter(r)
        c = circumference(r)
        display2(r, d, c)
    if x == 3:
        print('-------------------------')
        for x in range(40, 29, -2):
            a = math.sqrt(x)

            print('{0:<10.2f} {1:10.2f}'.format(x, a))
        print('-------------------------')
    if x == 4:
        id = initialDeposit1()
        ar = annualRate0fInterest1()
        mri = monthlyRate0fInterest(ar)
        display3(id, mri)
    if x == 5:
        y = 8
        while y != 4:
            menu1()
            y = y1()
            if y == 1:
                cletter()
            if y == 2:
                pop()
            if y == 3:
                area()
            if y == 4:
                break
    if x == 6:
        z = int(input("Enter a number:"))
        e = int(input("Enter a number:"))
        if z % 2 == 0:
            print("z is even")
        if z % 2 == 1:
            print("z is odd")
        if e % 2 == 0:
            print("e is even")
        if e % 2 == 1:
            print("e is odd")
        if z > 0 and e > 0:
            print("Both Positive numbers")
        if z < 0 and e < 0:
            print("Both negative numbers")
        if z > 100 or e > 100:
            print("Big number")
        else:
            print("ooooo..... Numbers")
    if x == 7:
        print('Thanks for running this program')
        break
