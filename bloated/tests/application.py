import unittest

from bloated import Application
from bloated.resources import Resource

from base import MockObject

class TestResource(Resource):

    pass


class MockApplication(Application):

    def __init__(self, **kwargs):
        routes = kwargs.pop('routes', None)
        super(MockApplication, self).__init__(**kwargs)
        self.routes = routes  # Set the routes.


class Request(MockObject):

    pass


class ApplicationTest(unittest.TestCase):

    def test_basic_routes(self):
        """ Testing the routes """

        # Positive tests
        app = MockApplication(routes={ '^/$': TestResource, })
        request = Request(path='/')
        (resource, kwargs) = app._map_resource(request)
        assert resource
        assert resource == TestResource

        app = MockApplication(routes={ '/.+/': TestResource, })
        request = Request(path='/abcd/')
        (resource, kwargs) = app._map_resource(request)
        assert resource
        assert resource == TestResource

        app = MockApplication(routes={ '/.+/': TestResource, })
        request = Request(path='/abcd/')
        (resource, kwargs) = app._map_resource(request)
        assert resource
        assert resource == TestResource

        # Negative tests
        app = MockApplication(routes={ '/.+/': TestResource, })
        request = Request(path='/')
        (resource, kwargs) = app._map_resource(request)
        assert not resource
        assert resource == None

        app = MockApplication(routes={ '/asdf/': TestResource, })
        request = Request(path='/')
        (resource, kwargs) = app._map_resource(request)
        assert not resource
        assert resource == None

        app = MockApplication(routes={ '^/$': TestResource, })
        request = Request(path='/asdf/')
        (resource, kwargs) = app._map_resource(request)
        assert not resource
        assert resource == None


    def test_arguments(self):
        """ Testing the routes """

        # Positive tests
        app = MockApplication(routes={ '/': TestResource, })
        request = Request(path='/')
        (resource, kwargs) = app._map_resource(request)
        assert resource
        assert resource == TestResource

        # Negative tests
        app = MockApplication(routes={ '/asdf/': TestResource, })
        request = Request(path='/')
        (resource, kwargs) = app._map_resource(request)
        assert not resource
        assert resource == None
