from api.design_wizard import PythonDW
from design.function_node import FunctionNode 
from design.field_node import FieldNode 

import json 
import glob 
import sys 


def pretty_print_function_restrict(files):
    for file_to_parser in files:
        
        
        print("\n")
        print("========================================================")    
        print("======Initializing Python Design Wizard ...=============")
        print("======File: {0}=============".format(file_to_parser))
        print("========================================================")     
        print("\n")

        dw = PythonDW()
        dw.parse(file_to_parser)

        for e in dw.get_all_functions():
            dw.create_function_entity(e)

        for e in dw.get_all_fields_without_class_func():
            dw.create_field_entity(e)
                 

        print("\n")
        print("===========Loading restricted functions...================")
        print("\n")
            
        functions_to_filter = restrict_json["functions_not_allowed"]

        func_entities_dw = dw.get_entity_by_type(FunctionNode)
        field_entities_dw = dw.entities.keys()

        print("\n")
        print("=========Filtering entities with the functions==========")
        print("\n")    

        functions_with_violations = {}

        for e in func_entities_dw:
            functions_with_violations[e.get_name()] = []
            for call in e.get_function_calls_str(just_caller=True):
                if call in functions_to_filter:
                    functions_with_violations[e.get_name()].append(call)

        for e in field_entities_dw:
            if e in functions_to_filter:
                for field in dw.entities[e]:
                    functions_with_violations[field.get_parent_name()] = e


        print("Done!")

        print("\n")
        print("======The following entities broke the restriction======")
        print("\n")                

        for k,v in functions_with_violations.items():
            print("{0} : {1}".format(k,v))    

def common_print_function_restrict(files, directory):
    
    print("\n")
    for file_to_parser in files:
        

        dw = PythonDW()
        dw.parse(file_to_parser)

        for e in dw.get_all_functions():
            dw.create_function_entity(e)

        for e in dw.get_all_fields_without_class_func():
            dw.create_field_entity(e)
                 

            
        functions_to_filter = restrict_json["functions_not_allowed"]

        func_entities_dw = dw.get_entity_by_type(FunctionNode)
        field_entities_dw = dw.entities.keys()


        functions_with_violations = {}

        for e in func_entities_dw:
            functions_with_violations[e.get_name()] = []
            for call in e.get_function_calls_str(just_caller=True):
                if call in functions_to_filter:
                    functions_with_violations[e.get_name()].append(call)

        for e in field_entities_dw:
            if e in functions_to_filter:
                for field in dw.entities[e]:
                    functions_with_violations[field.get_parent_name()] = e
              
        test_result = []
        for k,v in functions_with_violations.items():
            #print("{0} : {1}".format(k,v))
            if type(v) == type([]):
                test_result += v
            else:
                test_result.append(v)
        
        if not test_result: 
            test_result.append(".")
        
        file_to_parser = file_to_parser[len(directory) + 1:]    
        
        print("{0} {1}".format(" ".join(test_result),file_to_parser))            
        
    print("\n")    

if len(sys.argv) != 4:
    print("======Run the script with 'python -m demo.demo_interact path/to/json dir/to/parse'=============")
    print("Exiting script")
    exit(1)
    
json_path, directory, scripts = sys.argv[1], sys.argv[2], sys.argv[3]    


json_path = "./{0}".format(json_path)
restrict_json = json.load(open(json_path))



print("\nDirectory: " + directory)

directory = "./{0}".format(directory)
files = glob.glob('{0}/*.py'.format(directory))

common_print_function_restrict(files,directory)
