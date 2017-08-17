import unittest, ast
from api.design_wizard import PythonDW


class TestDesignWizard(unittest.TestCase):

	def test_default_values(self):
		dw = PythonDW()
		self.assertEqual(dw.ast_tree, [])
		self.assertEqual(dw.ast_elements_dict, {"class":ast.ClassDef,"function":ast.FunctionDef})
	
	def test_values_after_parse_file(self):
		dw = PythonDW()
		dw.parse("tests/data/simple_module.py")
		self.assertEqual(dw.get_all_classes(), ['Test','Test2'])
		self.assertEqual(dw.get_all_functions(), ['func1','func2'])
		
		
			

if __name__ == '__main__':
    unittest.main()        


		
"""
print "PRINTING INITIAL AST TREE: " + str(dw.ast_tree) + "\n"

print "PRINTING INITIAL AST ELEMENTS TO LOOK FOR INTO THE TREE: " + str(dw.ast_elements_dict) + "\n"

print "PARSING FILE: 'tests/data/simple_module.py' \n"
dw.parse("tests/data/simple_module.py")

print "GETTING ALL CLASSES: " 
dw.get_all_classes()

print "\n"

print "GETTING ALL FUNCTIONS: "
dw.get_all_functions()
"""
