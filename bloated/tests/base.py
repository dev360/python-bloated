

class MockObject(object):
    """
    Mockobject to create an object from dicts or key-val args.
    
    >>> user = MockObject({'id': 1234, 'username': 'ctoivola'})
    >>> user.id
    1234
    >>> user.username
    'ctoivola'

    >>> user = MockObject(id=1234, username='ctoivola')
    >>> user.id
    1234
    >>> user.username
    'ctoivola'

    """
    
    def __init__(self, *args, **kwargs):
        if args:
            for arg in [arg for arg in args if hasattr(arg, 'keys')]:
                for key in arg.keys():
                    self.__setattr__(key, arg[key])

        for key in kwargs:
            self.__setattr__(key, kwargs[key])


