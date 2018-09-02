def test_bubblesort(self):
    self.assertEqual(self.dw.get_all_classes_str(), \
     ['Test','Test2'])
    self.assertEqual(self.dw.get_all_functions_str(), \
     ['func1','func2', 'inside_func'])
    self.assertEqual(self.dw.get_all_imports_str(), \
     ['Math','unittest'])
     
 """
 
 TODO(Simple bubblessort test)
 
 step-by-step
 
 - Get all entities
 - Filter for entity
 - Filter nested for
 - Check for assign 
 - Return test result 
 
  REFACTOR DESIGN WIZARD
 
 
 def test(self):
  
 
 
 
 """
