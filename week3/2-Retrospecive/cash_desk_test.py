import unittest
from cash_desk import Bill, BatchBill, CashDesk


class CashDeskTest(unittest.TestCase):

    def setUp(self):
        self.bill = Bill(10)
        self.batch = BatchBill([Bill(5), Bill(10), Bill(15)])
        self.desk = CashDesk()

    def test_type_of_amount(self):
        with self.assertRaises(TypeError):
            Bill("10")

    def test_value_of_amount(self):
        with self.assertRaises(ValueError):
            Bill(-5)

    def test_batchbill_total(self):
        self.assertEqual(self.batch.total(), 30)

    def test_take_money_from_bill(self):
        self.desk.take_money(self.bill)
        self.assertEqual(self.desk.gold, 10)

    def test_take_money_from_batch(self):
        self.desk.take_money(self.batch)
        self.assertEqual(self.desk.gold, 30)

    def test_cashdesk_total(self):
        self.desk.take_money(self.bill)
        self.desk.take_money(self.batch)
        self.assertEqual(
            self.desk.total(), 'We have a total of 40$ in the bank')

    def test_cashdesk_inspect_value(self):
        self.desk.take_money(self.bill)
        self.desk.take_money(self.batch)
        self.desk.inspect()

if __name__ == '__main__':
    unittest.main()
