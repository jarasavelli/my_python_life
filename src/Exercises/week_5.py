#Exercises for collections


'''
Write a python script that can take mydict = {‘Bellevue’: ‘Microsoft’, ‘Seattle’: ‘Amazon’, ‘Everett’:’Boeing’} and print
Microsoft started in Bellevue
Amazon started in Seattle
Boeing started in Everett
Write a python script that can take mydict = {‘Bellevue’: ‘Microsoft’, ‘Seattle’: ‘Amazon’, ‘Everett’:’Boeing’} and sort (hint: sorted global function) the dictionary and print
Amazon started in Seattle
Boeing started in Everett
Microsoft started in Bellevue
Write a python script that can take mydict1 = {‘House1’: 1000, ‘House2’: 3000, ‘House3’: 5000} and mydict2 = {‘House1’: 6000, ‘House3’: 8000, ‘House2’: 6000} and to combine two dictionary adding values for common keys.
Output should be mydict3={‘House1’: 7000, ‘House2’: 9000, ‘House3’: 13000}
Write a python script that can take mydict={‘House1’: 7000, ‘House2’: 9000, ‘House3’: 13000} and print two largest values in the dictionary.
Hint: use nlargest function in heapq module
Write a python script that can take x = 3, using loops create three key and value pairs disctionary {1:1, 2:4, 3:6}. If key = 1, value is 1+1, for 2 value is 2+2, etc.
Write a python script that can take x = 3, using loops create key and value pairs disctionary {4:2, 9:3, 16:4}. If key = 4, value sqrt(4) is 2, for 9 value is 3, etc.
Hint: use pow function in Math module
Write a python script that can take x = 3, using loops create key and value pairs disctionary {1:1, 2:8, 3:27}. If key = 2, value pow(2) is 8, for 3 value is 27, etc.
Hint: use pow function in Math module

Functions
Create a function mystatenamelist  that can take string statename parameter and add to a list. Call that function and add up to 5 states.
Create a function mystateinfodict that can take string statename and string statecode parameters and add to a dictionary (key = statecode, value = statename) and add upto 5 states.
Create a function findmystatename that can take statecode parameter and return statename for the 5 states you created in problem 2.
Create a function delmystatename that can take statecode parameter and delete statename if it exists in the list you created in problem 2.
Write a Python function that accepts a string parameter and calculate the number of upper case letters and lower case letters and returns it.
Write a Python function sumoflist that can take a list with all numbers and calculate the sum of a list of numbers and returns it. Use recursive function, if possible.
Write a python function myfactorial that takes n as parameter to calculate the factorial number and returns it. Use recursive function, if possible.

'''

def funct_1(head_quarters, to_sort=False):

    items = head_quarters.items()
    if (to_sort):
        items = sorted(items,reverse=True)
    for key,value in items:
        print ("{value} started in {key}".format(key=key, value=value))

def find_n_largest(list,n):
    from heapq import nlargest
    return nlargest(n,list)

def create_dict(list, formula):

    from math import sqrt

    my_dict = dict()
    for i in list:
        if (formula == 0):
            my_dict[i] = i*2 # double
        elif (formula == 1):
            my_dict[i] = int(sqrt(i)) #sqrt
        elif (formula == 2):
            my_dict[i] = pow(i,2) #power
        i += 1
    return my_dict

def create_mystatelist(name,my_state_list):
    #
    my_state_list.append(name)

def create_state_dict(code,name,dict):
    #
    dict[code] = name

def find_state(code,dict):
    #
    return dict[code]

def remove_state(code,dict):
    #
    if (find_state(code,dict) != None):
        dict.pop(code)

def find_upper_lower(word):
    #
    uppercount = 0
    lowercount = 0
    chars = list(word)
   # print(chars)
    for c in chars:
        if chr(ord(c)).isupper():
            uppercount += 1
        else:
            lowercount += 1
    return uppercount, lowercount

def add_in_recursion(nums):

    if (len(nums)==1):
        return nums[0]
    else:
        return  nums[0] + add_in_recursion(nums[1:])

def factorial(num):
    if (num < 2):
        return 1
    else:
        return num * factorial(num-1)

def factorialByLoop(num):
    #
    factorial = num
    i = 1
    while (i < num):
        factorial *= num - i
        i += 1
    return factorial

if __name__ == '__main__':
    my_dict = {'Bellevue': 'Microsoft', 'Seattle': 'Amazon', 'Everett':'Boeing'}
  #  funct_1(my_dict)
  #  funct_1(my_dict, True)

    mydict1 = {'House1': 1000, 'House2': 3000, 'House3': 5000}
    mydict2 = {'House1': 6000, 'House3': 8000, 'House2': 6000}
    mydict1.update(mydict2)
    mydict3 = dict(mydict1)

 #   print(mydict3)
    mydict1 = {'House1': 7000, 'House2': 9000, 'House3': 13000}
    largest_values = find_n_largest(mydict3.values(),2)
 #   print("The two largest values are: {} , {}".format(largest_values[0],largest_values[1]))

 #  print(create_dict([1,2,3],0))
 #  print(create_dict([4,9,16],1))
 #  print(create_dict([1,2,3],2))

my_state_list = []
create_mystatelist("Washington",my_state_list)
create_mystatelist("Oklahoma",my_state_list)
create_mystatelist("Michigan",my_state_list)
create_mystatelist("Florida",my_state_list)
create_mystatelist("California",my_state_list)

#print(my_state_list)

state_dict = {}
create_state_dict("WA","Washington",state_dict)
create_state_dict("OK","Oklahoma",state_dict)
create_state_dict("MI","Michigan",state_dict)
create_state_dict("FL","Florida",state_dict)
create_state_dict("CA","California",state_dict)

#print(state_dict)

#print(find_state("CA",state_dict))
#remove_state("CA",state_dict)
#print(state_dict)

#s = input("Enter the string with mixed chars")
#u,l = find_upper_lower(s)
#print("The number of upper chars and lower chars in the '{}' are ({},{})".format(s,u,l))

sum = 0
print(add_in_recursion([1,2,3,4,5,6,7,8,9,]))
print (sum)

print(factorial(5))
import sys
import time
sys.setrecursionlimit(10000)
start_time = time.time()
print (factorial(9998))
print (time.time() - start_time)
start_time = time.time()
print (factorialByLoop(9998))
print (time.time() - start_time)

from src.HackerRank import algorithms_1

print(algorithms_1.flatlandSpaceStations(5, [0, 4]))