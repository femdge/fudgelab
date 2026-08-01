import random as rand


def rng():

    count = 0
    blue = 0
    pink = 0
    gray = 0
    orange = 0
    n = int(input("input desired number of desired trials\n"))

    while count < n:

        num = rand.randint(1, 100)

        if num < 41:
            orange+=1

        if 40 < num < 66:
            blue +=1

        if 65 < num < 91:
            pink +=1

        if 90 < num:
            gray +=1

        count+=1

    print("Blue: " + str(blue) + " (" + str(100*(blue/n)) + "%)\n"
        "Pink: " + str(pink) + " (" + str(100*(pink/n)) + "%)\n"
        "Gray: " + str(gray) + " (" + str(100*(gray/n)) + "%)\n"
        "Orange: " + str(orange) + " (" + str(100*(orange/n)) + "%)\n")

def coinToss():

    n = int(input("input desired number of desired coint tosses\n"))
    count = 0
    heads = 0
    tails = 0

    while count < n:

        num = rand.randint(0, 1)

        if num == 0:
            heads+=1
        else:
            tails +=1

        count +=1

    print("Expected heads: " + str(int(n/2)) + " (50%)" +
          "\n Actual heads: " + str(heads) + " (" + str(100*heads/n) + "%)" +
          "\n Expected tails: " + str(int(n/2)) + " (50%)" +
          "\n Actual tails: " + str(tails) + " (" + str(100*tails/n) + "%)")

q = input("Activate random number generator or coin flipper? (answer rng or cointoss)\n")

if q == "rng":
    rng()
elif q == "cointoss":
    coinToss()
else:
    print("input not understood")

