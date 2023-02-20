#Suppose that a machine sells bottles of Coca-Cola (Coke)
#for 50 cents and only accepts coins in these denominations:
#25 cents, 10 cents, and 5 cents.

#A program that prompts the user to insert a coin, one at a time,
#each time informing the user of the amount due.
#Once the user has inputted at least 50 cents,
#output how many cents in change the user is owed.
#Assume that the user will only input integers,
#and ignore any integer that isn’t an accepted denomination.

totalCoin=0

while totalCoin <50:


    print("Insert coins")
    userCoin = int(input())
    if userCoin not in(5,10,25):
        print("Amount Due: " + str((50-totalCoin)))
        continue
    totalCoin = (totalCoin+userCoin)
    if totalCoin < 50:
        print("Amount Due: " + str((50-totalCoin)))
    else:
        print("Change Owed: " + str((50-totalCoin)).replace('-',''))