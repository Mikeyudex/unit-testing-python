import unittest

from test_bank_account import BankAccountTests


def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests("test_deposit"))
    suite.addTest(BankAccountTests("test_withdraw"))
    return suite

if __name__ == "__main__":
    #Se instancia el runner para ejecutar la suite
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())

#comando para ejecutar la suite
#PYTHONPATH=. python tests/test_suites.py