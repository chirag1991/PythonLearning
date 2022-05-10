

name = input("Enter your name")

age = input("Enter your age")
data_type = type(age)
print(data_type)

#casting string age from integer age
age = int(age)
data_type = type(age)
print(data_type)


print("Hello,", name, "Your age is ", age)
# same message on different ways

Hellomessage = "Hello {} your age is {}".format(name,age)
print("This is from Hello message : ",Hellomessage);

Hellomessage1 = f"Hello {name} your age is {age}"
print("This is from different way of Hello message1 : ",Hellomessage1);











