import unittest
from design import entity as entity
from util.type_entity_enum import *

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

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEntityModule)
    unittest.TextTestRunner(verbosity=2).run(suite)        
