from api.design_wizard import PythonDW
from design.function_node import FunctionNode 
from design.field_node import FieldNode 
from tests.scripts.test_selected_scripts import TestModules

import json 
import glob 
import sys, os 
import subprocess
from subprocess import call as call_sp
import unittest

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
            
        functions_to_filter = restrict_functions_json["functions_not_allowed"]

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
        try:
            dw.parse(file_to_parser)
        except:
            print("Parse_error {0}".format(file_to_parser))
            continue
                

        for e in dw.get_all_functions():
            dw.create_function_entity(e)
            for field in e.body:
                dw.create_field_entity(field)
            

        for e in dw.get_all_fields_without_class_func():
            dw.create_field_entity(e)
                 
        functions_to_filter = restrict_functions_json["functions_not_allowed"]

        func_entities_dw = dw.get_entity_by_type(FunctionNode)  
        field_entities_dw = dw.get_entity_by_type(FieldNode)


        functions_with_violations = {}

        for e in func_entities_dw:
            functions_with_violations[e.get_name()] = []
            for call in e.get_function_calls_str(just_caller=True):
                if call in functions_to_filter:
                    functions_with_violations[e.get_name()].append(call)

        for e in field_entities_dw:
            if e.get_name() in functions_to_filter:
                if dw.entities.get(e.get_name()) is not None:
                    for field in dw.entities.get(e.get_name()):
                        functions_with_violations[field.get_parent_name()] = e.get_name()
            
              
        test_result = []
        for k,v in functions_with_violations.items():
            #print("{0} : {1}".format(k,v))
            if type(v) == type([]):
                test_result += v
            else:
                test_result.append(v)
        
        if not test_result: 
            test_result.append(".")
        
        file_to_parser = file_to_parser[len(directory):]    
        
        print("{0} {1}".format(" ".join(test_result),file_to_parser))            
        
    print("\n")  
    

def common_print_scripts_restrict(scripts_files, files):
    f = open(os.devnull, 'w')
    
    print("\n")
    results = {}
    for file_to_parse in files:
  

        dw = PythonDW()
        try:
            dw.parse(file_to_parse)
        except:
            print("Parse_error {0}".format(file_to_parse))
            continue
            
        sufix = len(".py")
        file_to_parse = file_to_parse[len(directory):]         
        results[file_to_parse] = []
        for script in scripts_files:
            path_script = "tests.scripts.{0}".format(script[:-sufix])
            name_test = script[:-sufix]

            test_loader = unittest.TestLoader()
            test_names = test_loader.getTestCaseNames(TestModules)

            suite = unittest.TestSuite()
            for test_name in test_names:
                suite.addTest(TestModules(test_name, dw, path_script, name_test))

            result = unittest.TextTestRunner(stream=f,descriptions=False).run(suite)
            if result.wasSuccessful():
                results[file_to_parse].append(".")
            else:
                results[file_to_parse].append(script[:-sufix])
                
    for k,v in results.items():
        print("{0} {1}".format(" ".join(v),k))
                    
    print("\n")

if len(sys.argv) != 5:
    print("======Run the script with 'python -m demo.demo_interact" +\
     " path/to/json dir/to/parse'=============")
    print("Exiting script")
    exit(1)
    
functions_json_path, directory, scripts_json_path, recursive = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

restrict_functions_json, restrict_scripts_json, scripts_files = [],[],[]


if functions_json_path != "" or False :
    if not functions_json_path[0] == "/":
        functions_json_path = "./{0}".format(functions_json_path)
    try:    
        restrict_functions_json = json.load(open(functions_json_path))
    except: 
        print("No such file: {0}\nExiting script;".format(functions_json_path))
        sys.exit(1)    
else:
    scripts_json_path = "{0}".format(scripts_json_path)
    try:
        restrict_scripts_json = json.load(open(scripts_json_path))
    except:
        print("No such file: {0}\nExiting script;".format(scripts_json_path))
        sys.exit(1)             
    scripts_files = restrict_scripts_json['scripts']
    


print("\nDirectory: " + directory)
      
if not directory[0] == "/":
    directory = "./{0}".format(directory)
        
if recursive == 't':
    if restrict_functions_json:
        folders = glob.glob('{0}/*'.format(directory))
        for direc in folders:
            print("Sub Directory: " + direc)
            temp_files = glob.glob('{0}/*.py'.format(direc))
            common_print_function_restrict(temp_files, direc)
    else:
        folders = glob.glob('{0}/*'.format(directory))
        for direc in folders:
            print("Sub Directory: " + direc)
            temp_files = glob.glob('{0}/*.py'.format(direc))
            common_print_scripts_restrict(scripts_files, temp_files)


else:
    files = glob.glob('{0}/*.py'.format(directory))

    if restrict_functions_json:
        common_print_function_restrict(files, directory)
    else:    
        common_print_scripts_restrict(scripts_files,files)
