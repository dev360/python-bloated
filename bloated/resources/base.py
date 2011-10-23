from types import MethodType

from bloated.exceptions import MethodNotAllowed, NotFound, InternalServerError 

class Resource(object):
    """ Represents a REST resource """


    def dispatch(self, request, **kwargs):
        """ Renders the resource """
        
        method = request.method.lower()
        response = None

        # 1. Check if method allowed
        allowed_methods = []

        if hasattr(self, 'Meta'):
            allowed_methods = [x.lower() for x in getattr(self.Meta, 'allowed_methods', [])]

        func = getattr(self, method) if hasattr(self, method) else None
        
        if method in allowed_methods:
            
            if not func:
                raise InternalServerError('%s(request, **kwargs) has not been defined on the resource' % method)

            if type(func) == MethodType:
                response = func(request, **kwargs)
            else:
                raise InternalServerError('%s is not a function' % method)

        else:
            raise MethodNotAllowed(valid_methods=allowed_methods)

        return response
