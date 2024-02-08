import unittest
from dict2 import Dict2

class TestDict2(unittest.TestCase):
    def test_store_and_access(self):
        obj = Dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3
        self.assertEqual(obj['a'], 1)
        self.assertEqual(obj['b'], 2)
        self.assertEqual(obj['c'], 3)

    def test_custom_exception(self):
        obj = Dict2()
        with self.assertRaises(KeyError):
            val = obj['a']

    def test_iterate_keys(self):
        obj = Dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3
        keys = [k for k in obj]
        self.assertEqual(keys, ['a', 'b', 'c'])

    def test_non_existing_key(self):
        obj = Dict2()
        obj['a'] = 1
        with self.assertRaises(KeyError):
            val = obj['b']

if __name__ == '__main__':
    unittest.main()
    
