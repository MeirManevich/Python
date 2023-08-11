def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    for a,b in enumerate(s):
            if a < 2:
                tf = b.isalpha()
    counter = 0
    for i in s:
        counter += 1
    if s.isalnum() and 2 <= counter <= 6 and tf == True:
        for i in s:
            if i.isnumeric():
                if i=="0":
                    return False
                else:
                    c = s.split(i)
                    d = "1"+c[1]
                    return d.isnumeric()
        else:
            return True


main()



#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate;
# AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”