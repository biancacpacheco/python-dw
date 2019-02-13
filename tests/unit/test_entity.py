import unittest, ast
from design import entity as entity
from util.type_entity_enum import EntityTypeEnum
from util.type_relation_enum import RelationTypeEnum
from api.design_wizard import PythonDW
from design.function_node import FunctionNode

class TestEntityModule(unittest.TestCase):

    def test_default_values(self):
        entity_1 = entity.Entity("Entity1",{})
        self.assertEqual(entity_1.name, 'Entity1')
        self.assertEqual(entity_1.type_entity, EntityTypeEnum.DEFAULT)
        self.assertEqual(entity_1.relations, {})
        self.assertEqual(entity_1.ast_node, {})
	
    def test_raise_exception_not_implemeted(self):
        entity_1 = entity.Entity("Entity2",{})
        with self.assertRaises(NotImplementedError) as cm:
            entity_1.get_name()
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Not implemented yet.")	



class TestFunctionEntityModule(unittest.TestCase):

    def setUp(self):
        self.dw = PythonDW()
        self.dw.parse("tests/data/function_module.py")
        
    def test_dafault_values_for_empty_function(self):
        self.dw.create_function_entity_by_name("empty_func")
        empty_func = self.dw.get_entity_by_name("def_empty_func")
        
        self.assertEqual(empty_func.get_name(), "empty_func")     
        self.assertEqual\
         (empty_func.get_function_calls(just_caller=True), [])
        self.assertEqual\
         (empty_func.get_function_calls(just_callee=True), [])

class TestParameterEntityModule(unittest.TestCase):
    pass    

class TestClassEntityModule(unittest.TestCase):
    
    def setUp(self):
        self.dw = PythonDW()
        self.dw.parse("tests/data/function_module.py")
        
    def test_add_relation(self):
        functions = self.dw.get_all_functions()
        for func in functions:
            self.dw.create_function_entity(func)
        
        function_entity = self.dw.entities.get("def_caller_func")
        self.assertNotEqual(function_entity.add_relation, {})

if __name__ == '__main__':
    print("\n== Testing General Entity ==")
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEntityModule)
    unittest.TextTestRunner(verbosity=2).run(suite) 
    
    print("\n== Testing Function entity ==")

    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctionEntityModule)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    print("\n== Testing Entity methods ==")
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestClassEntityModule)
    unittest.TextTestRunner(verbosity=2).run(suite)              
