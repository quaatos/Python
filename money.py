# Enter your first currency
first = input("first currency: ")
if (first != "dollar" and first != "euro" and first != "pound"):
    print("that currency is not in our database, quiting...")
    exit()

# Enter your second currency
second = input("second currency: ")
if (second != "dollar" and second != "euro" and second != "pound"):
    print("that currency is not our database, quiting...")
    exit()

# ask te amount of money
amount = float(input("How much money do you want to exchange: "))

# euro to dollar
number1 = 1.4389
if (first == "euro" and second == "dollar"):
    print(amount / number1 * 1.612)

# dollar to euro
number2 = 0.88
if (first == "dollar" and second == "euro"):
    print(amount * number2)

# pound to euro
number3 = 1.15
if (first == "euro" and second == "pound"):
    print(amount * number3)

# euro to pound
if (first == "pound" and second == "euro"):
    print(amount / number3)

# Dollar to pound
if (first == "dollar" and second == "pound"):
    print(amount * 0.65)

# Pound to dollar
if (first == "pound" and second == "dollar"):
    print(amount * 1.4635)

# created by Quaatos with <3
