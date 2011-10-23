from werkzeug.exceptions import HTTPException, NotFound, BadRequest, \
        MethodNotAllowed, Forbidden, NotAcceptable, RequestTimeout, \
        Conflict, Gone, LengthRequired, PreconditionFailed, \
        RequestEntityTooLarge, RequestURITooLarge, UnsupportedMediaType, \
        RequestedRangeNotSatisfiable, ExpectationFailed, InternalServerError, \
        NotImplemented, BadGateway, ServiceUnavailable, HTTPUnicodeError, \
        ClientDisconnected


class InvalidRouteError(Exception):

    def __init__(self, msg=None, **kwargs):
        route = kwargs.pop('route', '')
        detail = kwargs.pop('detail', '')
        super(Exception, self).__init__(msg or "The route '%s' is not a valid regex. \n\tDetails: %s" % (route, detail))
