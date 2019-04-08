def exercise_1(_x,_y):
    if _x > _y:
        print(str(_x) +" is greater than "+ str(_y))
    elif _x < _y:
        print(str(_x) +" is less than "+str(_y))
    else:
        print (str(_x) +" is equal to "+str(_y))
        
def exercise_2():
    x = 9
    y = 1
    while x >= y:
        print(str(x), end=" ")
        x = x - 1

def exercise_2_1(x,y,swap):
    if swap:
        temp = y
        y = x
        x = temp
        while x >= y:
            print(str(x), end=" ")
            x = x - 1
    else:
        while x <= y:
            print (str(x), end=" ")
            x = x + 1
        
def exercise_3():
    print()
    _numbers = [1,2,3,4,5]
    for i in _numbers :
        print(i, end=" ")


def exercise_3_1():
    print()
    _numbers = [1,2,3,4,5]
    for i in range(len(_numbers),0,-1) :
        print(_numbers[i-1], end=" ")
    
def exercise_4():
    _numbers = [1,2,3,4,5]
    for i in _numbers:
        if i <= 4:
            print(i, end=" ")

def exercise_4_1():
    _numbers = [1,2,3,4,5]
    print()
    for i in _numbers:
        if i != 4:
            print (i, end=" ")

def exercise_7() :
    _cities = ["Seattle", "LA", "NY","CA"]
    for _city in _cities:
        if _city.__eq__("NY"):
            print(_city)

def exercise_7_1(_cities, _ocity,_ncity):
    i = 0
    for _city in _cities :
        if _city.__eq__(_ocity):
            _cities[i] = _ncity
            break
        i += 1
    return _cities

print ("Exercise 1")
print ("============")
exercise_1(1,9)

print ("Exercise 2")
print ("============")
exercise_2()
print()
print ("Exercise 2_1 (1,9, swap=false)")
exercise_2_1(1,9,False)
print()
print ("Exercise 2_1 (1,9, swap=True)")
exercise_2_1(1,9,True)

print ("Exercise 3")
print ("============")
exercise_3()
exercise_3_1()



print ("\nExercise 4.1")
print ("============")
exercise_4()
exercise_4_1()

print ("\nExercise 7")
print ("============\n")
exercise_7()
print('\n')
print(exercise_7_1(["SEATTLE",'NY','LA','CA'],'NY','BOSTON'))
