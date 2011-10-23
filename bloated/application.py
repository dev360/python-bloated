import re

from werkzeug.wrappers import Request, Response

from exceptions import HTTPException, NotFound, InternalServerError

class Application(object):

    def __init__(self, **kwargs):
        super(Application, self).__init__()

    def __call__(self, env, start_response):
        return self.dispatch(env, start_response)

    def dispatch(self, env, start_response):
        """ Dispatches the application """

        request = Request(env)
        response = None

        try:
            (resource, kwargs) = self._map_resource(request)

            if resource:
                pass
            
        except HTTPException  as e:
            response = e
        except Exception as e:
            response = InternalServerError(description=str(e))

        # Default fallback is 404 not found.
        if response == None:
            response = NotFound()

        return response(env, start_response)

    @property
    def _routes(self):
        routes = getattr(self, 'routes', None)

        if not routes:
            raise HttpError(u'No routes have been specified for this application')

        return routes

    def _map_resource(self, request):
        """ Returns the resource and the keyword arguments """

        routes = self._routes
        url = request.path

        # TODO: Werkzeug Map class? Not sold on the notation though :-/

        for (route, resource) in routes.items():

            pattern = re.compile(route, re.IGNORECASE)
            match = pattern.match(url)
            if match:
                return (resource, {})

        return (None, None)

