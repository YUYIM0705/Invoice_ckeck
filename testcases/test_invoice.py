from src.invoice import get_last_n_numbers, get_max_matches_for_win_num

def test_get_last_3_numbers():
    ticket = '94899145'
    last_3_digits = get_last_n_numbers(ticket, 3)
    assert last_3_digits == '145'

def test_get_last_8_numbers():
    ticket = '94899145'
    last_8_digits = get_last_n_numbers(ticket, 8)
    assert last_8_digits == '94899145'

def test_get_3_matches_for_win_num():
    ticket = '94899145'
    win_num = '94898145'
    max_matches = get_max_matches_for_win_num(ticket,win_num)
    assert max_matches == 3

def test_get_no_matches_for_win_num():
    ticket = '94899145'
    win_num = '94898045'
    max_matches = get_max_matches_for_win_num(ticket,win_num)
    assert max_matches == 0

def test_get_8_matches_for_win_num():
    ticket = '94899145'
    win_num = '94899145'
    max_matches = get_max_matches_for_win_num(ticket,win_num)
    assert max_matches == 8