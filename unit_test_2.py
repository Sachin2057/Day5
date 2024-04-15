import unittest

import unittest.test
from mean_median import calculation

class TestCalculaion(unittest.TestCase):
    
    
    def test_empty_list(self):
        result=calculation([])
        self.assertIsNone(result["mean"])
        self.assertIsNone(result["std"])
        self.assertIsNone(result["median"])
    
    
    def test_single_elemt(self):
        first_result=calculation([1])
        self.assertAlmostEqual(first_result["mean"],1.0)
        self.assertAlmostEqual(first_result["median"],1.0)
        self.assertAlmostEqual(first_result["std"],0.0)
    
    def test_multiple_element(self):
        result=calculation([1,2,3])
        self.assertAlmostEqual(result["mean"],2.0)
        self.assertAlmostEqual(result["median"],2.0)
        self.assertAlmostEqual(result["std"],0.816)
        result=calculation([1,3,5,7,2])
        self.assertAlmostEqual(result["mean"],3.6)
        self.assertAlmostEqual(result["median"],3.0)
        self.assertAlmostEqual(result["std"],2.154)
if __name__=="__main__":
    unittest.main()