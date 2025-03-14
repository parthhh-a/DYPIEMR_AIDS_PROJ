def isPrime(n):
    '''
    Checks for a prime number.<br>
    Input - `n`, any integer <br>
    Output - boolean value
    '''
    c=0
    for i in range(2,n):
        if n%i==0:
            c=c+1


    if c==0 and n!=1:
        return 1
    else:
        return 0

###############################

def sum(a,b):
    '''
    Adds to numbers
    input: a, b - two numbers
    output: returns sum
    '''
    c=a+b
    return c

###############################

def difference(a,b):
   '''
   subtracts two numbers
   input: a, b - two numbers
   output: returns difference
   '''
   c=a-b
   return c

###############################

def Fibonacci_Series(n):
    # base case
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (Fibonacci_Series(n-2) + Fibonacci_Series(n-1))

###############################

def MultiplyTwoNumbers(a,b):
    """
    multiplying two numbers
    input: a,b - two numbers
    output: returns multiplication
    """
    c = a*b
    return c

###############################

def MultiplyList(myList):
    """
    multiplying the numbers in list
    input: list
    output: returns the multiplication
            of numbers in given list
    """
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

################################

def ConvertToDegree(radian):
    """
    Converts radian to degree
    input: angle in radian
    output: angle in degree
    """

    radian = float(radian)
    pi = 22/7
    degree = float(radian * (180 / pi))
    return degree

################################

def ConvertToRadian(degree):
    """
        Converts degree to radian
        input: angle in degree
        output: angle in radian
        """
    degree = float(degree)
    pi = 22 / 7
    radian = float(degree * (pi / 180))
    return radian
  
################################

def exponent(base, index):
    '''
    finds the exponent 
    input:two numbers -base and index 
    ouptut- base raised to the index
    '''
    if index == 0:
        return 1
    while index > 1:
        x = base**index
        return x

################################

def Perimeter(a,b,c):
    return (a+b+c)
a= int(input("Enter length of first side: \n"))
b= int(input("Enter length of second side: \n"))
c= int(input("Enter length of third side: \n"))
print("The perimeter of triangle is", Perimeter(a,b,c))


################################






