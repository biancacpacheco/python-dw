import unittest, ast
from api.design_wizard import PythonDW


class TestDesignWizard(unittest.TestCase):

	def test_default_values(self):
		dw = PythonDW()
		self.assertEqual(dw.ast_tree, [])
		self.assertEqual(dw.ast_elements_dict,\
		 {"class":ast.ClassDef, \
		 "function":ast.FunctionDef, \
		 "import":ast.Import })
	
	def test_values_after_parse_file_get_all_functions(self):
		dw = PythonDW()
		dw.parse("tests/data/simple_module.py")
		self.assertEqual(dw.get_all_classes_strings(), ['Test','Test2'])
		self.assertEqual(dw.get_all_functions_strings(), ['func1','func2', 'inside_func'])
		self.assertEqual(dw.get_all_imports_strings(), ['Math','unittest'])
		
	def test_values_of_inner_functions(self):
		dw = PythonDW()
		dw.parse("tests/data/simple_module.py")			
		self.assertEqual(dw.get_functions_inside_class("Test2"), ['inside_func'])
	
	def test_body_not_empty_function(self):
		dw = PythonDW()
		dw.parse("tests/data/simple_module.py")			
		self.assertNotEqual(dw.get_body_function("inside_func"), [])		
		
			

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDesignWizard)
    unittest.TextTestRunner(verbosity=2).run(suite)


