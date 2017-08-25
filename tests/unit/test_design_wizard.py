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
        self.assertEqual(dw.get_all_classes_str(), ['Test','Test2'])
        self.assertEqual(dw.get_all_functions_str(), ['func1','func2', 'inside_func'])
        self.assertEqual(dw.get_all_imports_str(), ['Math','unittest'])

    def test_values_of_inner_functions(self):
        dw = PythonDW()
        dw.parse("tests/data/simple_module.py")			
        self.assertEqual(dw.get_functions_inside_class_str("Test2"), ['inside_func'])

    def test_body_not_empty_function(self):
        dw = PythonDW()
        dw.parse("tests/data/simple_module.py")			
        self.assertNotEqual(dw.get_body_function("inside_func"), [])

    def test_get_fields_from_function(self):
        dw = PythonDW()
        dw.parse("tests/data/simple_module.py")
        self.assertEqual(dw.get_fields_function_str("func1"), ['oi'])       			

    def test_get_element_by_name(self):
        dw = PythonDW()
        dw.parse("tests/data/simple_module.py")
        self.assertEqual(dw.get_class_by_name("Test").name, 'Test')
        self.assertNotEqual(dw.get_class_by_name("Test"), [])
        
        self.assertEqual(dw.get_function_by_name("func1").name, 'func1')         
        self.assertNotEqual(dw.get_function_by_name("func1"), [])
        
        self.assertEqual(dw.get_import_by_name("Math").name, 'Math')
        self.assertNotEqual(dw.get_import_by_name("Math"), [])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDesignWizard)
    unittest.TextTestRunner(verbosity=2).run(suite)


