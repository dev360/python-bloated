from werkzeug.wrappers import Request, Response


class Application(object):

    def __init__(self, **kwargs):
        self.routes = kwargs.get('routes', {})
        super(Application, self).__init__()

    def __call__(self, env, start_response):
        request = Request(env)
        response = Response('Test')
        return response(env, start_response)

    def dispatch(self, env, start_response):
        """ Dispatches the application """

        try:
            pass
        except HttpError:
            pass

        # 1. Check if the resource exists
        request = Request(env)
        response = Response('Test')
        return response(env, start_response)

    def handle_404(self, env, start_response):

        return True

