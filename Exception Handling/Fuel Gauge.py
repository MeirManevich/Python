#a program that prompts the user for a fraction, 
#formatted as X/Y, wherein each of X and Y is an integer, 
#and then outputs, as a percentage rounded to the nearest integer, 
#how much fuel is in the tank. If, though, 1% or less remains, 
#output E instead to indicate that the tank is essentially empty. 
#And if 99% or more remains, output F instead to indicate that the tank is essentially full.

#If, though, X or Y is not an integer, X is greater than Y, or Y is 0, 
#instead prompt the user again. (It is not necessary for Y to be 4.) 
#Be sure to catch any exceptions like ValueError or ZeroDivisionError.


def main():
    while True:
        try:
            tank = input("Fraction:")
            a,b = tank.split("/")
            fraction = round(int(a)/int(b), 2)
            percentage = int(fraction*100)
            if(percentage<=1):
                print("E")
                break
            elif(99 <= percentage <= 100):
                print("F")
                break
            elif(percentage>100):
                pass
            else:
                print(str(percentage)+"%")
                break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass



main()