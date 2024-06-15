

# A
myDict = dict()

myDict["name"] = input("What is your name: ")
myDict["year"] = input("What's the current year: ")
myDict["hairColor"] = input("What's your hair color: ")
myDict["birthYear"] = input("What your birth year: ")
myDict["age"] = int(myDict["year"]) - int(myDict["birthYear"])

print(myDict)

print("Hello", myDict["name"], "you have", myDict["hairColor"], "hair.")
print("The current year is", myDict["year"])
print("You were born in", myDict["birthYear"])
print("That means you will be", myDict["age"], "years old this year")

# B
base = int(input("Please input the height: "))
height = int(input("Please input the base: "))

triangle_area = (1/2)*(base * height)

print("The area of the given triangle is:", int(triangle_area))

# C
numIn = input("Input two numbers, separated by a space: ")
newNum = numIn.split()

# print(type(newNum))
sum = int(newNum[0]) + int(newNum[1])
comparison = sum > 10
print("The sum of these two numbers is: ", sum)
print("Is the sum greater than 10?: ", comparison)