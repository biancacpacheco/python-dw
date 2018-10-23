import unittest, ast
from util.type_entity_enum import EntityTypeEnum
from util.type_relation_enum import RelationTypeEnum
from api.design_wizard import PythonDW
from design.function_node import FunctionNode
from design.relation.relation import Relation

class TestDesignWizard(unittest.TestCase):
    
    def setUp(self):
        self.dw = PythonDW()
        self.dw.parse("tests/data/simple_module.py")
    
    
    def test_default_values(self):
        design_wizard = PythonDW()
        self.assertEqual(design_wizard.ast_tree, [])
        self.assertEqual(design_wizard.entities, {})
        self.assertTrue\
         (set(["class","function","import","call","expression"]).\
         issubset(set(design_wizard.ast_elements_dict.keys())))


    def test_values_after_parse_file_get_all_functions(self):
        self.assertEqual(self.dw.get_all_classes_str(), \
         ['Test','Test2'])
        self.assertEqual(self.dw.get_all_functions_str(), \
         ['func1','func2', 'inside_func'])
        self.assertEqual(self.dw.get_all_imports_str(), \
         ['Math','unittest'])


    def test_values_of_inner_functions(self):
        self.dw.create_class_entity_by_name("Test2")
        self.assertNotEqual(self.dw.entities, [])
        class_entity1 = self.dw.get_entity_by_name("Test2")	
     		
        self.assertEqual\
         (class_entity1.get_functions_str(), \
         ['inside_func'])


    def test_body_not_empty_function(self):
        self.dw.create_function_entity_by_name("inside_func")
        self.assertNotEqual(self.dw.entities, [])
        func_entity1 = self.dw.get_entity_by_name("def_inside_func")	
        self.assertNotEqual\
         (func_entity1.get_function_fields_body(), [])


    def test_get_parameters_from_function(self):
        self.dw.create_function_entity_by_name("func2")
        function = self.dw.get_entity_by_name("def_func2")
        parameters = function.get_parameters_function_str()
        self.assertEqual(parameters, [])  
        
        self.dw.create_function_entity_by_name("func1")
        function = self.dw.get_entity_by_name("def_func1")
        parameters = function.get_parameters_function_str()
        self.assertEqual(parameters, ['r_param'])        			


    def test_get_element_by_name(self):
        self.assertEqual(self.dw.get_class_by_name("Test").name, 'Test')
        self.assertNotEqual(self.dw.get_class_by_name("Test"), [])
        
        self.assertEqual\
         (self.dw.get_function_by_name("func1").name, 'func1')         
        self.assertNotEqual(self.dw.get_function_by_name("func1"), [])
        
        self.assertEqual\
         (self.dw.get_import_by_name("Math").name, 'Math')
        self.assertNotEqual(self.dw.get_import_by_name("Math"), [])


    def test_get_entity_attribute_by_name(self):
        empty_node = FunctionNode("Empty",{}, initialize_elements=False)
        self.dw.entities["Empty"] = empty_node
        self.assertEqual\
         (self.dw.get_entity_by_name("Empty"), empty_node)


    def test_create_function_node_and_check_relation(self):
        
        ONLY_ELEMENT_LIST = 0
        
        self.dw.create_function_entity_by_name("func1")
        self.assertNotEqual(self.dw.entities, [])
        func_entity = self.dw.get_entity_by_name("def_func1")
        self.assertEqual(func_entity.get_name(), 'func1')
        
        self.assertNotEqual(func_entity.relations, {})
        
        relation = func_entity.get_relations_by_type\
         (RelationTypeEnum.HASFIELD)
        self.assertNotEqual(relation,[])
        self.assertEqual(type(relation), type([]))
        self.assertEqual\
         (relation[ONLY_ELEMENT_LIST].get_str_relation(), \
         'func1 HASFIELD r_param')
  
        
    def test_create_function_node_and_update_callee_status(self):
        # Order matters here because this update command is inside
        # node's creation.
        self.dw.create_function_entity_by_name("func2")
        self.assertNotEqual(self.dw.entities, [])
        func_entity2 = self.dw.get_entity_by_name("def_func2")
        self.assertEqual(func_entity2.get_name(), 'func2')
        
        self.dw.create_function_entity_by_name("func1")
        self.assertNotEqual(self.dw.entities, [])
        func_entity1 = self.dw.get_entity_by_name("def_func1")
        self.assertEqual(func_entity1.get_name(), 'func1')
        

        relation_calls = [e.get_str_relation() \
         for e in func_entity2.relations.get('ISCALLED')]
        
        self.assertEqual\
         (relation_calls, ['func2 ISCALLED func1'])
    
    
    def test_get_calls_inside_functions_body(self):
        self.dw.create_function_entity_by_name("func1")
        self.assertNotEqual(self.dw.entities, [])
        func_entity = self.dw.get_entity_by_name("def_func1")
        self.assertEqual(func_entity.get_name(),'func1')
        
        self.assertEqual(func_entity.get_function_calls_str(), \
         [ ('caller', ['func2']), ('callee', []) ] )
        self.assertEqual(func_entity.get_function_calls_str\
         (just_caller=True), ['func2'])        
        self.assertEqual(func_entity.get_function_calls_str\
         (just_callee=True), [])
       
         
    def test_delete_single_element_from_entities(self):
        self.dw.create_function_entity_by_name("func1")
        self.dw.create_function_entity_by_name("func2")
        self.dw.create_class_entity_by_name("Test")
        self.dw.create_class_entity_by_name("Test2")
        
        self.assertNotEqual(self.dw.entities, {})
        
        self.assertTrue("def_func1" in self.dw.entities)
        self.assertTrue("def_func2" in self.dw.entities)
        self.assertTrue("Test" in self.dw.entities)
        self.assertTrue("Test2" in self.dw.entities)
        
        self.dw.delete_entity_by_name("Test")
        
        self.assertTrue("def_func1" in self.dw.entities)
        self.assertTrue("def_func2" in self.dw.entities)
        self.assertTrue("Test2" in self.dw.entities)

        self.assertTrue("Test" not in self.dw.entities)

        
    def test_delete_all_elements_from_entities(self):
        self.dw.create_function_entity_by_name("func1")
        self.dw.create_function_entity_by_name("func2")
        self.dw.create_class_entity_by_name("Test")
        self.dw.create_class_entity_by_name("Test2")
        
        self.assertNotEqual(self.dw.entities, {})
        
        self.assertTrue("def_func1" in self.dw.entities)
        self.assertTrue("def_func2" in self.dw.entities)
        self.assertTrue("Test" in self.dw.entities)
        self.assertTrue("Test2" in self.dw.entities)
        
        self.dw.delete_all_entities()
        
        self.assertEquals(self.dw.entities, {})

    def test_updating_function_calls(self):
        self.dw.create_function_entity_by_name("func1")
        self.dw.create_function_entity_by_name("func2")
        self.dw.create_function_entity_by_name("inside_func")
        func2 = self.dw.get_entity_by_name("def_func2")
        
        self.assertEquals\
         (func2.get_function_calls_str(just_callee=True),['func1'])
         
        i =  self.dw.get_entity_by_name("def_inside_func")
        self.assertEquals\
         (i.get_function_calls_str(just_caller=True),['print','map','sort'])
           
    def test_get_expression_nodes(self):
        fields = self.dw.get_all_fields_without_class_func()
        fields_str = []
        for e in fields:
            self.dw.create_field_entity(e)
        self.assertEquals(list(self.dw.entities.keys()), ['sort',\
          'func2', 'for', 'map', 'sum', 'range', 'split',\
          'assign_field', 'raw_input', 'if'])
   
    def test_nested_for_sorting_algorithm(self):
        LAST_ADDED_FOR = -1
        LAST_ADDED_ASSIGN = -2
        
        fields = self.dw.get_all_fields_without_class_func()
        nested_fields = []
        for e in fields:
            self.dw.create_field_entity(e)
        for x in self.dw.entities.get('for'):
            nested_fields += x.get_nested_loops()

        leaf = self.dw.entities.get('assign_field')[LAST_ADDED_ASSIGN]
        branch = self.dw.entities.get('for')[LAST_ADDED_FOR]

    
        self.assertTrue( leaf.get_name() in ('tuple','subscript','index'))
        self.assertEqual( branch.ast_node, nested_fields[LAST_ADDED_FOR] )
        self.assertTrue( self.dw.is_leaf_from_branch(branch,leaf) )
  
    def test_if_in_segment(self):
        fields = self.dw.get_all_fields_without_class_func()
        nested_fields = []
        for e in fields:
            self.dw.create_field_entity(e)
        
        test = False
        for e in self.dw.entities.get("if"):
            if "ast.In" in str(e.ast_node.test.ops[0]):
                test = True
        
        self.assertTrue(test)        
                    
    def test_split_with_raw_input(self):
        fields = self.dw.get_all_fields_without_class_func()
        for e in fields:
            self.dw.create_field_entity(e)
        
        
        test = True
        for e in self.dw.entities.get("split"):
            relations = e.relations.get("ISCALLED") if \
             e.relations.get("ISCALLED") is not None else [] 
            
            test = False if not relations else True
            
            for split_relation in relations:
                if split_relation.get_callee_str() != "raw_input":
                    test = False
        
        self.assertTrue(test) 
        
    def test_get_calls_fields_by_name(self):
        num_field_calls = self.dw.get_field_calls_by_name("print")
        self.assertTrue(num_field_calls > 0)

    def tearDown(self):
        self.dw = []
             

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase\
     (TestDesignWizard)
    unittest.TextTestRunner(verbosity=2).run(suite)


