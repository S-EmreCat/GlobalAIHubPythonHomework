# -*- coding: utf-8 -*-
first_name=input("Please enter your FirstName: ")
last_name=input("Please enter your last name: ")
age=int(input("Please enter your age: "))
date_of_birth=int(input("Please enter date of birth year: "))

User_Info=[first_name,last_name,age,date_of_birth]

if User_Info[2]<18:
    print("You cant go out because it's too dangerous.")
    for info in User_Info:
        print(info)
else:
    for info in User_Info:
        print(info)
    print("You can go out to the street.")
