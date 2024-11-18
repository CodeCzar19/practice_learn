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
else:
    print("No your age is not 20")
if is_new_patiet == True:
    print("Yes He is a new patient.")
else:

    print("you are not patient")

secret_number = 10
guess_count = 1
guess_limit = 3
while guess_count <= 3:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print( "you won")
        break
else:
    print("sorry you failed.")

command = "" 
while True:
       command = input(">").lower()
       if command == "start":
          print("The car is started.")
       elif command == "stop":
           print("the car is stoped.")
       elif command == "help":
           
           print("""
start - to start the car
stop - to stop the car
exit - to exit 
                 """)
       elif command == exit:
           print("The car is exit.")
           break 
       else:
           print("sorry I don't understand.")
           