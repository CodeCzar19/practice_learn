course = 'Python for "Beginners" '
print(course)
# for multiple message
message = """
Hi Bilaxyan,
Would you like to join our online courese?
If you are interested. Please fill the form.
i love you aakash 

"""
another = message[:]  # for index character
print(another)

name = "Aakash"
print(name[0] + name[-1])

first_name = "Aakash"
last_name = "Rajdhami"
message = first_name + " [" + last_name + "] " "is a coder."
msg = f"{first_name} {last_name} is a coder."
print(msg)
input = "This is your first programming language."
print(input.upper())  # for upper case
print(f"Thre are {len(input)} elements.")  # for counting elements
print(f"L is in the {(input.find("l"))} place.")
print(input.replace("programming", "high level "))
print(input.replace("p", "a"))
print("level" in input)
