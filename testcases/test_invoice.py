from src.invoice import get_last_n_numbers

def test_get_last_3_numbers():
    ticket = '94899145'
    last_3_digits = get_last_n_numbers(ticket, 3)
    assert last_3_digits == '145'

def test_get_last_8_numbers():
    ticket = '94899145'
    last_8_digits = get_last_n_numbers(ticket, 8)
    assert last_8_digits == '94899145'