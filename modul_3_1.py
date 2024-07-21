calls = 0


def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info(string):
    count_calls()
    l_ = (len(string), string.upper(), string.lower())
    return l_


def is_contains(string, list_to_search):
    count_calls()
    for x in list_to_search:
        if len(x) == len(string):
            k = 0
            for i in range(len(x)):
                if string[i] == x[i].upper() or string[i] == x[i].lower():
                    k = k + 1
            if k == len(x):
                return True

    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print()
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print()
print(calls)
