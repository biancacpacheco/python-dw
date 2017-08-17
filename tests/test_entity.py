import unittest
from design import entity as entity

class TestEntityModule(unittest.TestCase):

    def test_default_values(self):
		entity_1 = entity.Entity("Entity1")
		self.assertEqual(entity_1.name, 'Entity1')
		self.assertEqual(entity_1.type_entity, entity.Enum.DEFAULT)
		self.assertEqual(entity_1.relations, {})
	
    def test_raise_exception_not_implemeted(self):
		entity_1 = entity.Entity("Entity2")
		with self.assertRaises(NotImplementedError) as cm:
			entity_1.get_name()
		the_exception = cm.exception
		self.assertEqual(the_exception.message, "Not implemented yet.")	

if __name__ == '__main__':
    unittest.main()        
