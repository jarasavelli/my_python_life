import math
#First take the string and measure the string (len)

def reverse(_str):
#    _str = "Welcome"
    if (_str == None):
        print ("Please enter a valild string")
    _len = len(_str)
    i = 1
    while (i <= _len):
        print (_str[_len - i],end="")
        i = i + 1


def findeven():
    numbers=[1,2,3,4,5,6,7,8,9,10]
    for x in numbers:
        if ((x%2)==0):
            print(x)
            
findeven()


#reverse("Sathish")
#print()
#reverse ("Josh")

        
 