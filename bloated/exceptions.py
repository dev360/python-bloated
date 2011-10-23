


class HttpError(Exception):
    """ Base HTTP error """

    default_status = 500
    default_message = u'Server Error'

    def __init__(self, message=None, **kwargs):
        
        if not message:
            message = self.default_message

        self.status = kwargs.pop('status', self.default_status)

        super(HttpError, self).__init__(message)
   

class NotFoundError(HttpError):
    """ Not found error """

    default_status = 404
    default_message = u'Not Found'


class MethodNotAllowedError(HttpError):
    """ Method not allowed error """

    default_status = 423
    default_message = u'Method not allowed'

