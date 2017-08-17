import unittest
from design.relation import relation as relation

class TestRelationModule(unittest.TestCase):

    def test_default_values(self):
		relation_1 = relation.Relation("A", "implements", "B")
		self.assertEqual(relation_1.get_caller(), 'A')
		self.assertEqual(relation_1.get_called(), 'B')
		self.assertEqual(relation_1.get_str_relation(), 'A implements B')
		

if __name__ == '__main__':
    unittest.main()        
