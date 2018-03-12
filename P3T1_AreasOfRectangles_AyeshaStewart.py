# CTI110
# AreaOf Rectangles
# Ayesha
# 2/27/2018

#gather information, define variables
L1 = float(input("Enter the length of rectangle one: "))

W1 = float(input("Enter the width of rectangle one: "))

L2 = float(input("Enter the length of rectangle two: "))

W2 = float(input("Enter the width of rectangle two: "))

#Calculations
area1 = L1 * W1
area2 = L2 * W2

if area1 > area2:
    print ("The first rectangle has the larger area")
elif area1 < area2:
    print ("The second rectangle has the larger area")
else:
    print ("Both rectangles have equal area")
