def test_split_with_raw_input(self):
    fields = self.dw.get_all_fields_without_class_func()
    for e in fields:
        self.dw.create_field_entity(e)
        
    split_occurrency = self.dw.entities.get("split") if \
     self.dw.entities.get("split") is not None else []     
    
    test = True
    for e in split_occurrency:
        relations = e.relations.get("ISCALLED") if \
         e.relations.get("ISCALLED") is not None else [] 
        
        test = False if not relations else True
        
        for split_relation in relations:
            if split_relation.get_callee_str() != "raw_input":
                test = False
    
    self.assertTrue(test)                     
