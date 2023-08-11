def main():
    fruit = input("Item: ").lower()
    calories = Calories(fruit)
    if calories == "":
        print("")
    else:
        print (f"Calories: {calories}")

def Calories(a):
    fruit_calorie = {
        "apple" : "130",
        "avocado" : "50",
        "banana" : "110",
        "Cantaloupe" : "50",
        "Grapefruit": "60",
        "grapes" : "90",
        "honeydew" : "50",
        "kiwifruit" : "90",
        "lemon" : "15",
        "lime" : "20",
        "nectarine" : "60",
        "orange" : "80",
        "peach" : "60",
        "pear" : "100",
        "pineapples" : "50",
        "plums" : "70",
        "strawberries" : "50",
        "sweet cherries" : "100",
        "tangerine" : "50",
        "watermelon" : "80"
    }
    if a in fruit_calorie:
        return fruit_calorie[a]
    else:
        return ""

main()