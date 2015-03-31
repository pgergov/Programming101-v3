import unittest
from bank_account import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Joro", 10, "BGN")

    def test_create_bank_account_class(self):
        self.assertTrue(isinstance(self.account, BankAccount))

    def test_is_name_valid_type(self):
        with self.assertRaises(TypeError):
            BankAccount(1000, 10, "BGN")

    def test_is_balance_valid_type(self):
        with self.assertRaises(TypeError):
            BankAccount("Joro", "gosho", "BGN")

    def test_is_currency_valid_type(self):
        with self.assertRaises(TypeError):
            BankAccount("Joro", 100, 1000)

    def test_is_balance_positive_number(self):
        with self.assertRaises(ValueError):
            BankAccount("Joro", -10, "BGN")

    def test_is_balance_private(self):
        with self.assertRaises(AttributeError):
            self.account.balance += 10

    def test_is_amount_being_deposited(self):
        old_balance = self.account.get_balance()
        self.account.deposit(10)
        new_balance = self.account.get_balance()
        self.assertEqual(10, new_balance - old_balance)

    def test_is_withdraw_possible_with_negative_number(self):
        self.assertFalse(self.account.withdraw(-10))

    def test_is_withdraw_possible_if_balance_not_enough(self):
        self.assertFalse(self.account.withdraw(20))

    def test_is_amount_multiple_by_10(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(5)

    def test_account_str_print(self):
        self.assertEqual(str(self.account), "Bank account for Joro with balance of 10BGN")

    def test_account_int_return(self):
        self.assertEqual(int(self.account), 10)

    def test_is_trasfer_possible_if_accounts_have_different_currencies(self):
        kiro = BankAccount("Kiro", 50, "$")
        self.assertFalse(self.account.transfer_to(kiro, 100))

    def test_history_of_account_that_is_just_created(self):
        self.assertEqual(["Account was created"], self.account.history())

    def test_history_after_some_actions(self):
        self.account.deposit(20)
        self.account.get_balance()
        int(self.account)
        self.account.withdraw(20)
        self.account.get_balance()
        self.account.withdraw(50)
        self.assertEqual(['Account was created', 'Deposited 20BGN', 'Balance check -> 30BGN', '__int__ check -> 30BGN', '20BGN was withdrawed', 'Balance check -> 10BGN', 'Withdraw for 50BGN failed.'], self.account.history())

if __name__ == '__main__':
    unittest.main()
