import unittest
from design.relation.relation import Relation
from design.function_node import FunctionNode

class TestRelationModule(unittest.TestCase):

    def test_default_values(self):
        func_a,func_b = FunctionNode("A",{}), FunctionNode("B",{})
        relation_1 = Relation(func_a, "implements", func_b)
        self.assertEqual(relation_1.get_caller(), func_a)
        self.assertEqual(relation_1.get_callee(), func_b)
        self.assertEqual(relation_1.get_str_relation(), 'A implements B')
		

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRelationModule)
    unittest.TextTestRunner(verbosity=2).run(suite)      
