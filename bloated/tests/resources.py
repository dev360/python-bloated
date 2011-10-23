import unittest

from bloated import Application
from bloated.resources import Resource
from bloated.exceptions import InvalidRouteError, MethodNotAllowed, \
        InternalServerError

from base import MockObject

class TestResource(Resource):

    def get(self, request, **kwargs):
        return { 'success': True }


    class Meta:
        allowed_methods = ['get', ]


class TestResourceMissingImpl(Resource):

    class Meta:
        allowed_methods = ['get','post']

class TestResourceBadImpl(Resource):
    
    get = 'blah'

    class Meta:
        allowed_methods = ['get','post']



class MockApplication(Application):

    def __init__(self, **kwargs):
        routes = kwargs.pop('routes', None)
        super(MockApplication, self).__init__(**kwargs)
        self.routes = routes  # Set the routes.


class Request(MockObject):

    pass        
    


class ResourceTest(unittest.TestCase):

    def test_allowed_methods(self):
        """ Testing allowed methods """
        
        # Positive tests
        
        # Method uppercase
        request = Request(method='GET')
        resource = TestResource()
        response = resource.dispatch(request, **{})
        
        assert response != None
        assert response == { 'success': True }

        # Negative tests

        request = Request(method='POST')
        resource = TestResource()
        self.assertRaises(MethodNotAllowed, resource.dispatch, request)


    def test_checks_method_defined(self):
        """ Tests that the application will throw a more informative 
        server error if the user forgot to define the method impl """

        request = Request(method='GET')
        resource = TestResourceMissingImpl()
        self.assertRaises(InternalServerError, resource.dispatch, request)


    def test_checks_method_is_function(self):
        """ Tests that the application will throw a more informative 
        server error if the user defined a method as a regular attribute and 
        not as a function """

        request = Request(method='GET')
        resource = TestResourceBadImpl()
        self.assertRaises(InternalServerError, resource.dispatch, request)

