text = input("text: ")
for i in text:
    if i == "a" or i == "e" or i=="i" or i=="o" or i=="u" or i == "A" or i == "E" or i=="I" or i=="O" or i=="U":
        text = text.replace(i,"")
print(text)