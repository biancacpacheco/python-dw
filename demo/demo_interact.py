from api.design_wizard import PythonDW
from design.function_node import FunctionNode 

print("\n")
print("======Welcome to Python Design Wizard demo==============")
print("\n")

file_to_parser = input("Enter the path to the file here: ")

print("\n")
print("======Initializing Python Design Wizard ...=============")
print("\n")

dw = PythonDW()
dw.parse(file_to_parser)

for e in dw.get_all_functions():
    dw.create_function_entity(e)
    
print("Done!")    

print("\n")
print("===========Restrict functions by name...================")
print("\n")
    
functions_to_filter = input\
 ("Enter the name of the functions to be " + \
 "restricted in files (separeted by space): ").split()

entities_dw = dw.get_entity_by_type(FunctionNode)

print("\n")
print("=========Filtering entities with the functions==========")
print("\n")    

functions_with_violations = {}

for e in entities_dw:
    functions_with_violations[e.get_name()] = []
    for call in e.get_function_calls_str(just_caller=True):
        if call in functions_to_filter:
            functions_with_violations[e.get_name()].append(call)

print("Done!")

print("\n")
print("======The following entities broke the restriction======")
print("\n")                

for k,v in functions_with_violations.items():
    print("{0} : {1}".format(k,v))    

