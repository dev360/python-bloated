import unittest

from bloated import Application
from bloated.resources import Resource
from bloated.exceptions import InvalidRouteError

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

        # One param
        app = MockApplication(routes={ '^/(?P<test1>[a-z]{3})/$': TestResource, })
        request = Request(path='/abc/')
        (resource, kwargs) = app._map_resource(request)
        assert resource
        assert resource == TestResource
        assert kwargs
        assert len(kwargs.keys()) == 1
        assert kwargs.keys()[0] == 'test1'
        assert kwargs.values()[0] == 'abc'
        
        # Multiple params
        app = MockApplication(routes={ '^/(?P<test1>[a-z]{3})/(?P<test2>[0-9]{3})/$': TestResource, })
        request = Request(path='/abc/123/')
        (resource, kwargs) = app._map_resource(request)
        assert resource
        assert resource == TestResource
        assert kwargs
        assert len(kwargs.keys()) == 2
        assert kwargs.keys()[0] == 'test1'
        assert kwargs.values()[0] == 'abc'
        assert kwargs.keys()[1] == 'test2'
        assert kwargs.values()[1] == '123'



        # Negative tests
        
        # no params
        app = MockApplication(routes={ '/asdf/': TestResource, })
        request = Request(path='/asdf/')
        (resource, kwargs) = app._map_resource(request)
        assert resource
        assert resource == TestResource
        assert kwargs != None
        assert kwargs == {}

    def test_raises_invalidroute(self):
        # Positive tests
        # Specify a broken regex!
        app = MockApplication(routes={ '/(asdf/': TestResource, })
        request = Request(path='/asdf/')
        self.assertRaises(InvalidRouteError, app._map_resource, request)
