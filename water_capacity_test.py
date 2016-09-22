import unittest

import water_capacity
import water_capacity_recursive


table = [
    ['empty', [], 0],
    ['one_trough', [4, 1, 1, 4], 6],
    ['two_troughs', [40, 1, 1, 4, 3, 7], 19],
    ['flat', [1, 1, 1, 1, 1, 1], 0],
    ['decreasing', [9, 8, 7, 6, 5, 4, 3, 2, 1], 0],
    ['borders', [0, 10, 0, 10, 0, 10, 0], 20]
]

class TestWaterCapacity(unittest.TestCase):

    def test_recursive(self):
        for name, array, excepted in table:
            result = water_capacity_recursive.water_capacity(array)
            self.assertEqual(result, excepted, '"{0}" test case failed (recursive)'.format(name))

    def test(self):
        for name, array, excepted in table:
            result = water_capacity.water_capacity(array)
            self.assertEqual(result, excepted, '"{0}" test case failed'.format(name))


if __name__ == '__main__':
    unittest.main()
