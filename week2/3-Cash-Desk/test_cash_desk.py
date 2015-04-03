import unittest
from cash_desk import Bill
# в unittest имаме клас TestCase, в него са дефинирани методите за сравняване


class CashDeskTest(unittest.TestCase):
    def test_create_new_bill_class(self):
        bill = Bill(10)
        self.assertTrue(isinstance(bill, Bill))

    def test_create_int_value_from_bill(self):
        bill = Bill(10)
        self.assertEqual(int(bill), 10)

    def test_amount_in_bill(self):
        bill = Bill(10)

        with self.assertRaises(AttributeError):
            bill.amount

if __name__ == '__main__':
    unittest.main()