def list_avg(arr):
    if type(arr) == list:
        if len(arr) > 0:
            total = 0
            for thing in arr:
                if type(thing) == int or type(thing) == float:
                    total += thing
                else:
                    raise TypeError('List elements must be numbers.')
            return total / len(arr)
        else:
            raise ValueError('List must have at least one element.')
    else:
        raise TypeError('Argument must be a list.')
            