import unittest
from StringCalculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def test_add_empty_str(self):
        test_data = ""
        correct_result = 0
        test_result = StringCalculator().add(test_data)
        self.assertEqual(correct_result, test_result)

    def test_add_one_argument(self):
        test_data = "1"
        correct_result = 1
        test_result = StringCalculator().add(test_data)
        self.assertEqual(correct_result, test_result)

    def test_add_two_number_with_comma(self):
        test_data = "10,30"
        correct_result = 40
        test_result = StringCalculator().add(test_data)
        self.assertEqual(correct_result, test_result)

    def test_add_two_number_with_enter(self):
        test_data = "10\n30"
        correct_result = 40
        test_result = StringCalculator().add(test_data)
        self.assertEqual(correct_result, test_result)

    def test_add_negative_number(self):
        test_data = "-10\n30\n-15"
        correct_result = "отрицательные числа запрещены: -10,-15"
        test_result = StringCalculator().add(test_data)
        self.assertEqual(correct_result, test_result)

    def test_add_three_number_with_enter(self):
        test_data = "10\n30\n15"
        correct_result = 55
        test_result = StringCalculator().add(test_data)
        self.assertEqual(correct_result, test_result)

    def test_add_number_greater_1000(self):
        test_data = "10\n30\n15,1001"
        correct_result = 55
        test_result = StringCalculator().add(test_data)
        self.assertEqual(correct_result, test_result)

    def test_add_with_separator(self):
        test_data = "//#\n1#2"
        correct_result = 3
        test_result = StringCalculator().add(test_data)
        self.assertEqual(correct_result, test_result)

    def test_add_with_long_separator(self):
        test_data = "//###\n1###2"
        correct_result = 3
        test_result = StringCalculator().add(test_data)
        self.assertEqual(correct_result, test_result)


if __name__ == '__main__':
    unittest.main()
