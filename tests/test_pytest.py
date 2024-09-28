import pytest
from src.bank_account import BankAccount

""" def test_sum():
    a = 4
    b = 4
    assert a + b == 8
 """

@pytest.mark.parametrize("amount, expected", [
    (100, 1100),
    (3000, 4000),
    (4500, 5500),
])
def test_deposit_multiple_amounts(amount, expected):
    account = BankAccount(balance=1000, log_file="transactions.txt")
    new_balance = account.deposit(amount)
    assert new_balance == expected

def test_deposit_negative_amount():
    account = BankAccount(balance=1000, log_file="transactions.txt")
    with pytest.raises(ValueError):
        account.deposit(-100)


@pytest.mark.parametrize("initial_balance, deposit_amount, expected_balance, exception", [
    (1000, -100, None, ValueError),   # Negative deposit should raise ValueError
    (1000, 200, 1200, None),          # Positive deposit should update balance
    (500, 300, 800, None),            # Another positive deposit
    (500, -50, None, ValueError),     # Another negative deposit
])
def test_deposit_amount(initial_balance, deposit_amount, expected_balance, exception):
    account = BankAccount(balance=initial_balance, log_file="transactions.txt")
    
    if exception:
        with pytest.raises(exception):
            account.deposit(deposit_amount)
    else:
        new_balance = account.deposit(deposit_amount)
        assert new_balance == expected_balance