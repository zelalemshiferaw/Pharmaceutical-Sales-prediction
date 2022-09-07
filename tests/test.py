
import unittest
import numpy as np
import sys
import os
from pprint import pprint
import json
sys.path.append('../')
from scripts.read_data import ReadData

class TestReadData(unittest.TestCase):

    def setUp(self) -> pd.DataFrame:
        self.loader = ReadData()

    def test_read_csv(self):
        ad_df = self.loader.read_csv('tests/test_dataset.csv')
        self.assertEqual(len(ad_df), 6)


if __name__ == '__main__':
    unittest.main()