def full_name(first, last):
    if type(first) == str and type(last) == str:
        return first + ' ' + last
    else:
        raise TypeError('Each argument must be a str.')