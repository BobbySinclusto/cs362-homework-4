def list_avg(arr):
    if type(arr) == list:
        if len(arr) > 0:
            total = 0
            for thing in arr:
            return total / len(arr)
        else:
            raise ValueError('List must have at least one element.')
    else:
        raise TypeError('Argument must be a list.')

if __name__ == '__main__':
    print(list_avg(eval(input())))
            