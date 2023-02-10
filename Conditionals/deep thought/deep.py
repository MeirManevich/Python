# a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

def main():
    TheAnswer=input('What is the answer to the Great Question of Life, the Universe and Everything? ').casefold().strip()
    if TheAnswer == '42' or TheAnswer == 'forty-two' or TheAnswer == 'forty two':
        print('Yes')
    else:
        print('No')

main()