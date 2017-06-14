try:
    s= None
    if s is None:
        print('S是None')
        raise NameError
    print(len(s))
except TypeError:
    print('空空对象长度为0')
