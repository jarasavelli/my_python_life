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


    #find biggest distanced cities
    max_distance = 0

    for i,scity in enumerate(c):
        if i+1!=scity_len:
            distance = abs(c[i] - c[i+1])
            if distance > max_distance:
                max_distance = distance


    if scity_len == n:
        return 0
    if n % 2 != 0:
        median_low_city= int((last_city + first_city)/2)
        median_high_city = median_low_city
    else:
        median_low_city = int((last_city + first_city) / 2)
        median_high_city = median_low_city + 1


    if max_distance%2 != 0:
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

#print(flatlandSpaceStations2(100,[93,41,91,61,30,6,25,90,97]))
#help(map)

# Complete the fairRations function below.
def isOdd(n):
    if int(n)%2 != 0:
        return True
    return False

def fairRations(B):

    bread_count = 0
    all_evens = False
    not_found = False
    while not_found == False and all_evens == False:
        for index, val in enumerate(B):
            if (index+1 < len(B)):
                if isOdd(B[index]):
                    B[index] = val+1
                    B[index+1] = B[index+1]+1
                    bread_count += 2
                    if isOdd(B[index+1]) == False:
                        all_evens = True
                else:
                    all_evens = True
            else:
                #
                if isOdd(B[index]):
                    not_found =  True
                    all_evens = False
                else:
                    all_evens = True
            index += 1

    if not_found:
        return "NO"
    else:
        return bread_count


#calling
#fairRations([2,3,4,5,6])

# Complete the cavityMap function below.
def cavityMap(grid):

    _breadth = _depth =  len(grid)
    cavity_grid = []
    new_grid_row = []
    for m,row in enumerate(grid):
        if m != 0 and m != _breadth - 1:  # non border row
            for n, element in enumerate(row):
                if n != 0 and n != _depth - 1: # non border column.
                    if element > grid[m-1][n] \
                        and element > grid[m+1][n] \
                        and element > grid[m][n-1] \
                        and element > grid[m][n+1]:

                        #
                        new_grid_row.append('X')
                    else:
                        new_grid_row.append(grid[m][n])
                else:
                    new_grid_row.append(grid[m][n])
        else:
            for element in grid[m]:
                new_grid_row.append(element)
        cavity_grid.append(''.join(e for e in new_grid_row))
        new_grid_row = []

    return cavity_grid

## Run
# grid = ['989','198','111']
#
# for row in grid:
#     print (row)
# new_grid = cavityMap(grid)
# for row in new_grid:
#     print (row)
#
# grid = ['1112',
#         '1912',
#         '1892',
#         '1234'
#         ]
#
# for row in grid:
#     print (row)
# new_grid = cavityMap(grid)
# for row in new_grid:
#     print (row)

# #


def gradingStudents(grades):
    # Write your code here

    rounded_grades = []

    for index,grade in enumerate(grades):
        if grade < 38:
            rounded_grades.append(grade)
        else:
            lower_diff = grade % 5
            if lower_diff == 0:
                rounded_grades.append(grade)
            elif 5 - lower_diff < 3:
                rounded_grades.append(grade+5-lower_diff)
            else:
                rounded_grades.append(grade)

    return rounded_grades


#print(gradingStudents([93,41,91,64,38,6,25,93,98]))

def unWrapped(matrix):

    m = len(matrix)
    n = len(matrix[0])
    total_elements = m*n
    count = 0
    layers = []
    unwrapped = []
    TOP_ROW = 0
    BOTTOM_ROW = m-1
    LEFT_COLUMN = 0
    RIGHT_COLUMN = n-1
    i = 0
    j = 0

    begin = i+j
    while count < total_elements:

        unwrapped.append(matrix[i][j])
        if i == BOTTOM_ROW:
            if j != LEFT_COLUMN:
                j = j - 1
            elif i != TOP_ROW:
                i = i - 1
            elif j != RIGHT_COLUMN:
                j += 1
        elif j == LEFT_COLUMN:
            if i != TOP_ROW:
                i = i - 1
            elif j != RIGHT_COLUMN:
                j = j+1
            elif i != BOTTOM_ROW:
                i += 1
        elif j == RIGHT_COLUMN:
            i = i + 1
        else:
            j = j+1

        if i == j and begin == i+j:
            layers.append(unwrapped)
            i += 1
            j += 1
            BOTTOM_ROW -= 1
            TOP_ROW  += 1
            LEFT_COLUMN += 1
            RIGHT_COLUMN -= 1
            unwrapped = []
            begin = i+j
        count += 1

    #print (layers)
    return layers


def changePosition(array, pos):

    pos = pos%len(array)
    array = array[pos:] + array[:pos]

    #print(array)
    return array

def wrapped(layers,matrix):
#


    m = len(matrix)
    n = len(matrix[0])
    total_elements = m*n
    count = 0
    TOP_ROW = 0
    BOTTOM_ROW = m-1
    LEFT_COLUMN = 0
    RIGHT_COLUMN = n-1
    i = 0
    j = 0
    index = 1

    begin = i+j
    layers.reverse()
    layer = layers.pop()

    while count < total_elements:

        matrix[i][j] = layer[index-1]

        if i == BOTTOM_ROW:
            if j != LEFT_COLUMN:
                j = j - 1
            elif i != TOP_ROW:
                i = i - 1
            elif j != RIGHT_COLUMN:
                j += 1
        elif j == LEFT_COLUMN:
            if i != TOP_ROW:
                i = i - 1
            elif j != RIGHT_COLUMN:
                j = j+1
            elif i != BOTTOM_ROW:
                i += 1
        elif j == RIGHT_COLUMN:
            i = i + 1
        else:
            j = j+1

        if i == j and begin == i+j:
            i += 1
            j += 1
            BOTTOM_ROW -= 1
            TOP_ROW  += 1
            LEFT_COLUMN += 1
            RIGHT_COLUMN -= 1
            if len(layers) != 0:
                layer = layers.pop()
            begin = i+j
            index = 0

        count += 1
        index += 1

    #print (matrix)
    return matrix

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
#
    layers = unWrapped(matrix)
    for index,layer in enumerate(layers):
        layers[index] = changePosition(layer,r)

    matrix = wrapped(layers,matrix)

    print('\n'.join([''.join(['{:<1} '.format(item) for item in row]) for row in matrix]))

if __name__ == "__main__":
#
    matrixRotation([[11,12,13,14,15,16],[21,22,23,24,25,26],[31,32,33,34,35,36],[41,42,43,44,45,46],[51,52,53,54,55,56]],7)