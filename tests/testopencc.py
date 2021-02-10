import unittest
import opencc


class OpenCCTest(unittest.TestCase):
    def test_s2t(self):
        converter = opencc.OpenCC('s2t')
        self.assertEqual('漢字', converter.convert('汉字'))
