#  a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 
# (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). 

def convert(yup):
    a= yup.replace(':)', '🙂').replace(':(', '🙁')
    return(a)

def main():
    b= convert(input('Please give input '))
    print(b)

main()