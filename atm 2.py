import unittest
import ATM_machine_homework


class TestCalc(unittest.TestCase):
    def test_subtraction(self):
        result = ATM_machine_homework.subtraction(100 - 20)
        self.assertEqual(result, 80)
        if __name__ == '__main__':
            unittest.main()
