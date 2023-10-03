print("This is practice for input data")
print("Please enter your name so I can capitalize it")

print("First method using title() function")
name = input()
nameCapitalized = name.title()
print("Hello:", nameCapitalized)

print("Second method using loops")
name2 = input()
# emir lopez armenta

nameSplitted = name2.split()

nameCapitalized2 = ""

for name in nameSplitted:
    nameCapitalized2 += name.capitalize() + " "

print("Hello: ", nameCapitalized2)
