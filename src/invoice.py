winning_numbers = ['94899145', '71143793', '41055355']
#unit test
def get_last_n_numbers(numbers, n):
    return numbers[-n:]

if __name__ == '__main__':
    ticket = '94899145'
    last_4_digits = get_last_n_numbers(ticket, 4)
    assert last_4_digits == '9145'

def get_max_matches_for_win_num(ticket,win_num):
    max_matches = 0
    for i in range(3,9):
        t = get_last_n_numbers(ticket,i)
        w = get_last_n_numbers(win_num,i)
        if t == w:
            max_matches = i
        else:
            break
    return max_matches

def get_max_matches_for_win_num(ticket,win_num):
    max_matches = 0
    for i in range(3,9):
        t = get_last_n_numbers(ticket,i)
        w = get_last_n_numbers(win_num,i)
        if t == w:
            max_matches = i
        else:
            break
    return max_matches
