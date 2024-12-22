#Typecasting: Changing one data type to another

name= "Han"
age= 27
gpa=3.2
employed=True

#If we want to know the data type we can use type function

type(name) #This wont print anything so we add a print fuction

print(type(name))
print(type(age))
print(type(gpa))
print(type(employed))

#This will display <class 'str'> <class 'int'> <class 'float'> <class 'bool'>

#To change explicitlly we can define the data type

age=float(age)
gpa=int(gpa)
employed=str(employed)
print(f"{age}\n{gpa}\n{employed}")

#when converting a number into boolean values, anything other than 0 will be True

age=bool(age)
print(age)

#Implicitly converting values means that a value is converted automatically

x=2
y=.7

x=x/y #This automatically converted the value into float

print(x) 

#If I want to keep it as an interger i could
x=2
y=.7

x=int(x/y)
print(x)
#or
x=2
y=.7

x=x//y
print(x)
