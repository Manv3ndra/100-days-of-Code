#BMI Calculator to demonstrate exceptions
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height**2
print(bmi)

try:
    file = open("test_file.txt")
    a_dict = {"key":"value"}
    print(a_dict["non-existent_key"])
except FileNotFoundError:
    file = open("test_file.txt", "w")
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError("Wrong Key")
