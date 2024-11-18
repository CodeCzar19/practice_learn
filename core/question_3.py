has_good_income = True
has_creminal_record = False

if has_good_income and not has_creminal_record:
    print(f"The employee is eligible for loan.")
else:
    print(f"The employee is not eligible for loan")

temperature = 7
if temperature >= 30:
    print(f"It is hot day.")
elif temperature <= 10:
    print(f"it is nether hor or cold.")

#if name is less than 3 characters long name must be at least 3 character 
# otherwise if it is more than 50n characters long name can be a maximum 50 character #
# otherwise name looks good
    name = "Bilaxyan"
    if len(name) < 3:
        print(f"Name must be 3 character.")
    elif len(name) > 50:
        print(f"Name must be 50 character.")
    else:
        print(f"name looks good.")

        weight = int(input("enter your weight:"))
        unit = str(input("enter 'L' for lbs and 'K' for kg:")).upper()

        if unit == "L":
           converted = weight * 0.45
           print(f"The weight is {converted} kg.")
        elif unit == "K":
            converted = weight/0.45
            print(f"The weight is {converted} lbs")

i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
    
print("It is good.") 

i = 5
while i > 0:
    print("*" * i)
    i = i - 1
print("good")
