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

def string_power():

    count = 0
    my_list = ["CAL","SEA", "PIT","CAL"]
    for _city in my_list:
        i = 0
        print ("city is"+_city)
        count=0
        while (i < len(my_list)):
            print("inside loop:"+_city+":"+my_list[i])
            if (_city == my_list[i]):
                count = count+1
                print("count is"+str(count))
            if (count >=2):
                my_list.__delitem__(i)
                break
            i = i+1

    print(my_list)

def string_power2():
    #
    count = 0
    i = 0
    my_list = ["CAL","SEA","PIT","CAL","POR","KEN","NJC"]
    while(i < len(my_list)):
        if ((i+1)%2 == 0):
            my_list[i] = "remove"
        i += 1
    for city in my_list:
        if city == "remove":
            my_list.remove(city)
    print(my_list)

def string_power3():
    #
    state_code_list = ["WA","CA"]
#    state_list = ["Washington", "California"]
    state_list = ["California", "Washington"]
    merged_list = state_code_list
    i = 0
    while(i < len(state_list)):
        state = state_list[i]
        j = 0
        for state_code in state_code_list:
            print(state); print(state_code)
            if (state_code == "WA" and state == "Washington"\
                or
                state_code == "CA" and state == "California"):
                #
                merged_list.insert(j+1,state)
                print(merged_list)
                break
            j += 1
        i += 1
    print(merged_list)

string_power3()
#findeven()


#reverse("Sathish")
#print()
#reverse ("Josh")

        
 