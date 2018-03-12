#CTI110
#Ayesha
#SoftwareSales
#03/08/18

#Variables
def main():
    
    copies=int(input("How many copies are you purchasing? "))
    item= 99
    initialCost= 99 * copies

#Calculations based on number of copies purchased
    if 10 <= copies <= 19:
        discount = initialCost * .10
        total= initialCost-discount
        print ("You get a 10% discount!")
        print ("Your total is $", format(total, ".2f"))
    elif 20 <= copies <= 49:
        discount = initialCost * .20
        total= initialCost-discount
        print ("You get a 20% discount!")
        print ("Your total is $", format(total, ".2f"))
    elif 50 <= copies <= 99:
        discount = initialCost * .30
        total= initialCost-discount
        print ("You get a 30% discount!")
        print ("Your total is $", format(total, ".2f"))
    elif 100 <= copies:
        discount = initialCost * .40
        total= initialCost-discount
        print ("You get a 40% discount!")
        print ("Your total is $", format(total, ".2f"))
    else:
        print ("Add more copies to get a discount!")

main ()
