

name = input("Enter your name")

age = input("Enter your age")
data_type = type(age)
print(data_type)

#casting string age from integer age
age = int(age)
data_type = type(age)
print(data_type)


print("Hello,", name, "Your age is ", age)



