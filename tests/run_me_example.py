import api.design_wizard as dw

dw = dw.PythonDW()

print "PRINTING INITIAL AST TREE: " + str(dw.ast_tree) + "\n"

print "PRINTING INITIAL AST ELEMENTS TO LOOK FOR INTO THE TREE: " + str(dw.ast_elements_dict) + "\n"

print "PARSING FILE: 'tests/data/simple_module.py' \n"
dw.parse("tests/data/simple_module.py")

print "GETTING ALL CLASSES: " 
dw.get_all_classes()

print "\n"

print "GETTING ALL FUNCTIONS: "
dw.get_all_functions()
