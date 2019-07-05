

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


if __name__ == "__main__":

    bdaygifts = BirthdayGifts("Taum")

    print bdaygifts.taumBday(10,10,1,1,1)

    print bdaygifts.taumBday(5,9,2,3,4)

    print bdaygifts.taumBday(3,6,9,1,1)

    print bdaygifts.taumBday(7,7,4,2,1)

    print bdaygifts.taumBday(3,3,1,9,2)

