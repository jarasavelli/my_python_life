

def my_factorial(_num):
    _facto = _num
    while _num > 1:
        _facto = _facto * (_num - 1)
        _num = _num -1
    return _facto
def my_factorial_2(_num):
    i = _num
    _facto = _num
    for i in range(_num,1,-1):
        _facto = _facto * (i-1)
    return _facto

print ("Please enter +ve integer for which you want to know factorial")
_in = input()
while _in.__ne__("quit"):
    
    if _in.isdigit():
        _in = int(_in)
        print ("Factorial using while:"+str(my_factorial(_in)))
        print ("Factorial using For:"+str(my_factorial_2(_in)))
        print ("Please enter +ve integer for which you want to know factorial")
    else:
        print("Oops, Please provide a +ve integer")
    
    _in = input()
print ("Thank for using Factorial")
