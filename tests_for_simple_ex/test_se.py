from simple_expression import func_se
from unittest import TestCase


class SimpleExpressionTestCase(TestCase):
    def test_1_1_1_return_minus_1(self):
        self.assertEqual(-1, func_se(1, 1, 1))

    def test_1_1_61_return_minus_61(self):
        self.assertEqual(-61, func_se(1, 1, 61))

    def test_0_0_5_return_minus_5(self):
        self.assertEqual(-5, func_se(0, 0, 5))

    def test_1_2_3_return_minus_5(self):
        self.assertEqual(-5, func_se(1, 2, 3))

    def test_5_5_5_return_minus_20(self):
        self.assertEqual(-20, func_se(5, 5, 5))
