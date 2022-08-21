import unittest
import Main

class BubbleSortTest(unittest.TestCase):

    def test_bubble_sort_1(self):
        expected = [0, 1, 2, 3]
        actual = Main.Array([3, 2, 1, 0]).bubblesort()
        self.assertEqual(expected, actual)

    def test_bubble_sort_2(self):
        expected = [-2, -1, 0, 1, 2]
        actual = Main.Array([1, -1, 2, -2, 0]).bubblesort()
        self.assertEqual(expected, actual)

    def test_bubble_sort_3(self):
        expected = [-10, -9, -1, 0, 1, 9, 10]
        actual = Main.Array([10, -10, 0, 1, -1, -9, 9]).bubblesort()
        self.assertEqual(expected, actual)

    def test_bubble_sort_4(self):
        expected = [-10, -10, -1, -1, 0, 0, 1, 1, 10, 10]
        actual = Main.Array([10, -10, 0, 1, -1, -10, 10, 0, -1, 1]).bubblesort()
        self.assertEqual(expected, actual)

    def test_bubble_sort_5(self):
        expected = []
        actual = Main.Array([]).bubblesort()
        self.assertEqual(expected, actual)

    def test_bubble_sort_6(self):
        expected = [-0.1, -0.003, 0.002, 0.1]
        actual = Main.Array([0.1, -0.1, 0.002, -0.003]).bubblesort()
        self.assertEqual(expected, actual)