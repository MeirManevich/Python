# a program that prompts the user for the name of a file and then outputs that file’s 
# media type if the file’s name ends, case-insensitively, in any of these suffixes:

def main():
    file = input('What is the name of your file?').casefold().strip()
    if file.endswith('.gif'):
        print('image/gif')
    elif file.endswith('.jpg') or file.endswith('.jpeg'):
        print('image/jpeg')
    elif file.endswith('.png'):
        print('image/png')
    elif file.endswith('.pdf'):
        print('application/pdf')
    elif file.endswith('.txt'):
        print('text/plain')
    elif file.endswith('.zip'):
        print('application/zip')
    else:
        print('application/octet-stream')

main()