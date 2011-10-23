import simplejson


class BaseRenderer(object):

    def serialize(self, obj):
        raise NotImplementedError()

    def deserialize(self, data):
        raise NotImplementedError()


class JSONRenderer(BaseRenderer):

    def serialize(self, obj):
        return simplejson.dumps(obj)

    def deserialize(self, data):
        return simplejson.loads(data)
