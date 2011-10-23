from werkzeug.wrappers import Request, Response

from exceptions import HttpError

class Application(object):

    def __init__(self, **kwargs):
        super(Application, self).__init__()

    def __call__(self, env, start_response):
        request = Request(env)
        response = Response('Test')
        return response(env, start_response)

    def dispatch(self, env, start_response):
        """ Dispatches the application """

        request = Request(env)

        try:
            routes = self._routes
            
        except HttpError as e:
            response = handle_error(request, e)
        except Exception as e:
            response = handle_error(request, HttpError(str(e)))

        return response(env, start_response)

    @property
    def _routes(self):
        routers = getattr(self, 'routes', None)

        if not routers:
            raise HttpError(u'No routes have been specified for this application')

        return routers

    def handle_error(self, request, error):
        
        return 



