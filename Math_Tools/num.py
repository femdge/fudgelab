import random as rand

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

