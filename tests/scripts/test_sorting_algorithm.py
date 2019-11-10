def test_sorting_algorithm(self):
    self.dw.design_populate_all_entities()
    self.assertTrue(
        self.dw.design_get_relations_from_entity('for1', 'HASLOOP') != [])
    node_callee = \
        self.dw.design_get_relations_from_entity(
            'for1', 'HASLOOP')[0].get_callee()
    assertation = self.dw.design_entity_has_type_as_child(
        node_callee, 'assign_field'
    )
    self.assertTrue(assertation)
