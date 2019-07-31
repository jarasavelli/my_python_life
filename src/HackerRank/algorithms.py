

class BirthdayGifts:

    def __init__(self,name):
        print "Initializing"
        self.name = name

    #
    # Complete the 'taumBday' function below.
    # The function is expected to return a LONG_INTEGER.
    # The function accepts following  parameters:
    # 1. INTEGER b
    # 2. INTEGER w
    # 3  INTEGE bc
    # 4. INTEGER wc
    # 5. INTEGER z
    ##

    def taumBday(self,b,  w,  bc,  wc,  z):

        #
        # Check to see if cost of conversion is less than the price difference between bc and wc
        # if it is, then use conversion and update the price of black or white with whichever is lowest +
        # cost-of-conversion

        if abs(bc - wc) > z:
            #use conversion
            if bc > wc:
                bc = wc+z
            else:
                wc = bc+z

        # now find the total cost
        return b*bc + w*wc


# Complete the organizingContainers function below.
def organizingContainers(container):
    #
    # check the length of the container
    # for each column in a row that does not match with row number
    # check if the total of values in other rows and column matching row you started with
    # if the total is greater than its impossible

    n = len(container)
    container_swaps_needed = []
    type_swaps_needed = []
    swaps_needed = 0

    i = 0
    while i < n:
        j = 0
        swaps_needed = 0
        while j < n:
            if i != j:
                swaps_needed += container[i][j]
            j += 1
        container_swaps_needed.append(swaps_needed)
        i += 1

    i = 0
    while i < n:
        j = 0
        swaps_needed = 0
        while j < n:
            if i != j:
                swaps_needed += container[j][i]
            j += 1
        type_swaps_needed.append(swaps_needed)
        i += 1

    if container_swaps_needed == type_swaps_needed:
        return "Possible"

    return "Impossible"



if __name__ == "__main__":

    #bdaygifts = BirthdayGifts("Taum")

    #print bdaygifts.taumBday(10,10,1,1,1)

    #print bdaygifts.taumBday(5,9,2,3,4)

    #print bdaygifts.taumBday(3,6,9,1,1)

    #print bdaygifts.taumBday(7,7,4,2,1)

    #print bdaygifts.taumBday(3,3,1,9,2)

    #container = [[1,1],[1,1]]

    #print organizingContainers(container)

    #container = [[0,2],[1,1]]

    #print organizingContainers(container)

    #container = [[1,3,1], [2,1,2],[3,3,3]]

    #print organizingContainers(container)

    #container = [[0,2,1], [1,1,1], [2,0,0]]

    #print organizingContainers(container)

    container = [[999336263,998799923],[998799923,999763019]]
    print organizingContainers(container)

    container = [[997612619,934920795,998879231,999926463],
                 [960369681,997828120,999792735,979622676],
                 [999013654,998634077,997988323,958769423],
                 [997409523,999301350,940952923,993020546]]
   # print organizingContainers(container)
    container = [[997427147,
    999234285,
    998319806],
    [993127006,
    999257405,
    999972351],
    [999251470,
    996489548,
    994064605]]
    print organizingContainers(container)