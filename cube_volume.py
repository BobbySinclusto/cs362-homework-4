def cube_volume(side_length):
    if type(side_length) == int or type(side_length) == float:
        if side_length < 0:
            raise ValueError('Side length must be at least 0.')
        return side_length ** 3
    else:
        raise TypeError('Side length must be a positive real number.')