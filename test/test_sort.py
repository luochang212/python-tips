"""test heap sort
   author: luochang212
   last update: 2020-06-20
"""

import unittest
import my_sort

class TestHeapSort(unittest.TestCase):
    """test heap sort with unittest"""

    def setUp(self):
        self.st = my_sort.SortTool()

    def test_isinstance(self):
        self.assertEqual(type(self.st.heap_sort()), type([]))

    def test_result(self):
        self.assertEqual(self.st.heap_sort([8, 3, 10]), [3, 8, 10])


if __name__ == '__main__':
    unittest.main()
