# Braydn Ballard
# UWYO COSC 1010
# November 04, 2024
# Lab 08
# Lab Section: 14
# Sources, people worked with, help given to:
# your
# comments
# here

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def floatcheck(stringvalue):
    if "." in stringvalue:
        try:
            float(stringvalue)
            return True
        except:
            return False
def intcheck(stringvalue):
    try:
        int(stringvalue)
        return True
    except:
        return False

iniof = input("What is your string?:")
def stringcheck(intorfloat):
    if floatcheck(intorfloat) == True:
        intorfloat = round(float(intorfloat), 1)
        print(f"{intorfloat} is a {type(intorfloat)} value.")
    elif intcheck(intorfloat) == True:
        intorfloat = int(intorfloat)
        print (f"{intorfloat} is a {type(intorfloat)} value.")
    else:
        print("This string cannot be turned into float or integer type.")

stringcheck(iniof)


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound

ylist = []
def y_return(m,b,lowb,upb):
    for x in range(lowb,upb+1):
        ylist.append(m*x+b)
def numcheck(valuein):
    try:
        float(valuein)
        return True
    except:
        return False

    
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
while True:
    formin = input("Write the function in the form: slope/y-intercept/lowerbound/upperbound:")
    if "exit" in formin.lower():
        break
    else:
        newformin = formin.split("/")
        if numcheck(newformin[0]) == True and numcheck(newformin[1])==True and intcheck(newformin[2])==True and intcheck(newformin[3])==True:
            y_return(float(newformin[0]),float(newformin[1]),int(newformin[2]),int(newformin[3]))
            print (ylist)
            ylist.clear()
        else:
            print("Not a valid input.")






print("*" * 75)


def poscheck(valin):
    try:
        if "-" not in str(valin):
            return True
        else:
            return False
    except:
        return False
def quadsqrt(a,b,c):
    value = (b**2)-(4*a*c)
    if poscheck(value) == True:
        value = value**.5
        return value
    else:
        return None
answerlist = []
def quadform(a,b,c):
    try:
        root = quadsqrt(a,b,c)
        value1 = (-1*b)+(root)/(2*a)
        value2 = (-1*b)-(root)/(2*a)
        answerlist.append(value1)
        answerlist.append(value2)
        print(answerlist)
    except:
        print("Not a valid Input.")

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
# If the number you are trying to take the square root of is negative, return null
while True:
    quadin = input("Input your a, b, and c in the following format: a/b/c. Input here:")
    if "exit" in quadin:
        break
    else:
        quadinfix = quadin.split("/")
        if numcheck(quadinfix[0])== True and numcheck(quadinfix[1])== True and numcheck(quadinfix[2])== True:
            quadform(float(quadinfix[0]),float(quadinfix[1]),float(quadinfix[2]))
            answerlist.clear()
        else:
            print("Not a valid input.")
        