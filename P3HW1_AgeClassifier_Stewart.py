# CTI-110 
# P3HW1 - Age Classifier 
# Ayesha Stewart
# 03/01/18
#

def main():
    
    age= int(input("Enter your age: "))

    if age <= 1:
        print ("You're an infant.")
    elif age > 1 and age < 13:
        print ("You're a child.")
    elif age >= 13 and age < 20:
        print ("You're a teenager.")
    else:
        print ("You're an adult")

main ()
