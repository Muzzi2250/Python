#Userinput we use the input function in order for the user to declare the variable

name=input("Enter your name: ")

#Lets say you want to add +1 in your age, first we will have to change the value to an interger of float since the input is originally a str
age = int(input("What is your age: "))
age=age+1

print(f"Hi {name}")
print(f"You are {age}")

#Exercise 1: Madlibs game 

adjective=input("Enter an adjective: ")
noun=input("Enter a noun: ")
adjective2=input("Enter an adjective: ")
adjective3=input("Enter an adjective: ")

print(f"I saw a {adjective} {noun}")
print(f"The {noun} was very {adjective2}")
print(f"I was genually {adjective3}")

#Exercise 2: Area of a rectangle 

x=int(input("What is the length of the rectangle: "))
y=int(input("What is the height of the rectangle: "))

z=x*y

print(f"The are of the rectangle is: {z}")

#Exercise 3: Shopping cart

items= input("What item would you like to purchase?: ")
price= float(input("How much is the item?: "))
quantity= int(input("How many would you like to buy?: "))

Total= price*quantity

print(f" You are purchasing {quantity} x {items}s ")
print(f"Your total would be $ {round(Total, 2)}")