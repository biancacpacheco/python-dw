def test_sorting_algorithm(self):
    fields = self.dw.get_all_fields_without_class_func()
    for e in fields:
        self.dw.create_field_entity(e)
    for loop in self.dw.entities['for']:
        self.dw.create_body_loop(loop)
    self.assertTrue(self.dw.get_entity_by_name('for1').get_relations_by_type('HASLOOP') != [])
    node_callee = self.dw.get_entity_by_name('for1').get_relations_by_type('HASLOOP')[0].get_callee()
    assertation = False
    for field in self.dw.entities.get('assign_field'):
        if self.dw.is_leaf_from_branch(node_callee, field):
            assertation = True

    self.assertTrue(assertation)