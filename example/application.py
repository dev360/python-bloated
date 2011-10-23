from bloated import Application
from resources import UserResource


class Application(Application):

    routes = {
        '^users/': UserResource,
        
    }
