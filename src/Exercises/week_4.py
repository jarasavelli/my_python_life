def compareTriplets(a, b):
    #
    bob_score = 0
    alice_score = 0
    if ((len(a) == 3) and (len(b) == 3)):
        for i in range(0,3):
            if(a[i] < b[i]):
                bob_score += 1
            elif (a[i] > b[i]):
                alice_score += 1
    else:
        return [0,0]
    return [alice_score,bob_score]

def aVeryBigSum(ar):
    #
    sum = int(0)
    for num in ar:
        sum += num;
    return sum

ar = [1000000001,1000000002,1000000003,1000000004,1000000005]
#print(aVeryBigSum(ar))


def diagonalDifference(arr):
    #
    l2r_diag = 0
    r2l_diag = 0
    r2l_slope = len(arr) + 1
    m = 0
    n = 0
    for row in arr:
        m += 1
        n = 1
        for element in row:
            if m == n:
                l2r_diag += int(element)
            if m+n == r2l_slope:
                r2l_diag += int(element)
            n += 1
    return abs(l2r_diag - r2l_diag)

def staircase(n):
    for i in range(0,n):
        breadth = n
        while (breadth > 0):
            if(breadth > i+1):
                print(' ',end='')
                breadth -= 1
            else:
                print("#",end='')
                breadth -= 1
        print()

def miniMaxSum(arr):
    arr = sorted(arr)
    print(arr)
    min = max = 0
    for index,num in enumerate(arr):
        if (index > 0):
            max += num
        if (index < len(arr) - 1):
            min += num
    print ("{} {}".format(min,max))

def timeConversion(s):
    #
    hands = s.split(':')
    if ((str(hands[2]).endswith("PM"))):
            hands[0] = int(hands[0]) + 12
            if (hands[0] == 24):
                hands[0] = 12
    elif((str(hands[2]).endswith("AM"))):
        if (hands[0] == "12"):
            hands[0]  = "00"
    hands[2] = hands[2].rstrip("APM")
    return "{}:{}:{}".format(hands[0],hands[1],hands[2])
#help(format)
    #

import math

def flatlandSpaceStations(n, c):
    #
    if (n == len(c)):
        return 0
    max_d=[]
    for i in range(0,n):
        max_d.append(n)
        for scity in c:
            if (i == scity):
                max_d[i] = 0
                break
            elif (max_d[i] > abs(scity-i)):
                max_d[i] = abs(scity-i)
    return max(max_d)

def flatlandSpaceStations2(n,c):
    #
    max_d=[]
    c = sorted(c)
    scity_len = len(c)
    first_city = min(0, n-1)
    last_city = max(0, n-1)
    first_scity_pos = 0
    last_scity_pos = scity_len-1

    if (scity_len == n):
        return 0
    if n % 2 != 0:
        median_low_city= int((last_city + first_city)/2)
        median_high_city = median_low_city
    else:
        median_low_city = int((last_city + first_city) / 2)
        median_high_city = median_low_city + 1


    if (scity_len) % 2 != 0:
        median_low_scity_pos = int((last_scity_pos + first_scity_pos) / 2)
        median_high_scity_pos = median_low_scity_pos
    else:
        median_low_scity_pos = int((last_scity_pos + first_scity_pos) / 2)
        median_high_scity_pos = median_low_scity_pos + 1

    #distace of first_city to first space station
    max_d.append(abs(first_city-c[0]))
    #distace of last_city to last space station
    max_d.append(abs(last_city-c[scity_len-1]))

    #median to first and last space stations
    for scity in c

    max_d.append(abs(median_high_city - c[median_high_scity_pos]))
    max_d.append(abs(median_high_city - c[median_low_scity_pos]))
    max_d.append(abs(median_low_city - c[median_high_scity_pos]))
    max_d.append(abs(median_low_city - c[median_low_scity_pos]))

    print(max_d)
    return max(max_d)
# calling
#miniMaxSum([3,1,5,9,7])
#print(compareTriplets([1,2,3],[3,3,3]))
#print(timeConversion("12:40:22AM"))

#ar = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
#print(diagonalDifference(ar))

#staircase(6)

print(flatlandSpaceStations2(100,[93,41,91,61,30,6,25,90,97]))
#help(map)