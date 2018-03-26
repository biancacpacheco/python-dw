import unittest, ast


class TestModules(unittest.TestCase):

    def __init__(self, testname, dw, path_test, name_test):
        super(TestModules, self).__init__(testname)
        self.path_test = path_test
        self.dw = dw
        self.name_test = name_test
        
        
    def test(self):
        method_to_call = getattr(__import__(self.path_test,\
         fromlist=[self.name_test]), self.name_test)
        result = method_to_call(self)
