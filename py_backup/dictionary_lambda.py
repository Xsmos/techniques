def dictionaryLambda():
    dict_func = \
        {
            'plus': lambda x, y: x + y,
            'minus': lambda x, y: x - y,
            'max': lambda x, y: max(x, y),
            'min': lambda x, y: min(x, y),
            'multi': lambda x, y: x*y,
            'divi': lambda x, y: x/y
        }

    print(dict_func['plus'](3,5))
    print(dict_func['minus'](3,5))
    print(dict_func['max'](3,5))
    print(dict_func['min'](3,5))
    print(dict_func['multi'](3,5))
    print(dict_func['divi'](3,5))

