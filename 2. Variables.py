#Types: String, interger, float, boolean

#Strings (These are letters)
first_name = "Seung Won"
last_name = "Han"
keyboard = "Rainy 75 pro"

print(first_name)

#To display with words and variables we use f-string by displaying f"text{variable}"

print(f"Hello {first_name} {last_name} ")
print(f"you are currently using a {keyboard} as a keyboard")

#You can also add spaces with \n command
print(f"Really\nNice!")

#Intergers (These are whjole numbers, they should never be in "" cause it would turn them into strings)

born_in= 1998
current_year= 2024

print(f"You were born in {born_in}, time flies as it is {current_year} right now")

#Floats (These are floating numbers, in other words they contain decimal numbers)

price= 10.99
gpa = 3.2

print(f"Today's meal was {price}")

#Booleans (These are True or False, normally you dont output them directly commonly used with if statements)

employed= True

print(f"Are you employed: {employed}")

print("사랑해")