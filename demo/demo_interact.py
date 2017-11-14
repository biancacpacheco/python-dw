from api.design_wizard import PythonDW

print("\n")
print("======Welcome to Python Design Wizard demo==============")
print("\n")

file_to_parser = input("Enter the path to the file here: ")

print("\n")
print("======Initializing Python Design Wizard ...==============")

dw = PythonDW()
dw.parse(file_to_parser)

for e in dw.get_all_functions():
    dw.create_function_entity(e)

    

