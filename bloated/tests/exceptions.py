import unittest

from bloated.exceptions import HttpError, NotFoundError, MethodNotAllowedError


class HttpErrorTest(unittest.TestCase):

    def test_constructor(self):
        """ Testing the constructor """

        ex1 = HttpError()
        assert ex1.status == 500
        assert str(ex1) == u'Server Error'

        ex2 = HttpError('XYZ Error', status=501)
        assert ex2.status == 501
        assert str(ex2) == u'XYZ Error'
        

