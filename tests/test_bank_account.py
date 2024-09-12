import unittest
import os

from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    #Este metodo se ejecuta al finalizar cada test
    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, 'El balance no es igual')

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, 'El balance no es igual')
    
    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000, 'El balance no es igual')
    
    def test_transaction_log(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"), 'El archivo transaction_log no existe')

    def test_count_transaction(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1, 'La cantidad de lineas del archivo no coinciden')
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2, 'La cantidad de lineas del archivo no coinciden')