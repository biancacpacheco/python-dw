def test_xpto(self):
    self.dw.design_populate_all_entities()
    self.assertTrue(
        self.dw.design_get_qtd_calls_function('print') == 1
    )
