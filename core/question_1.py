# We check a patient name Jonh smith. He is 20 years old and is a new patient.

given_name = "John smith"
given_age = 20
is_new_patiet = False

to_check_name = str(input("Enter name: "))
to_check_age = int(input("Enter age: "))


if to_check_name == given_name:
    print("yes you are John smith.")
else:
    print("No you are not John")

if to_check_age == given_age:
    print("yes you are 20 years old.")
elif is_new_patiet == True:
    print("Yes He is a new patient.")
else:

    print("you are not patient")
