import cherrypy
import os
import sys

class HelloWorld(object):
    def __init__(self, media):
        self.media = media

    @cherrypy.expose
    def index(self):
        return open(f'site/{self.media}/index.html')

media = sys.argv[1]
port = sys.argv[2]
if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './site/public'
        }
    }
    cherrypy.config.update({'server.socket_port': int(port)})
    cherrypy.quickstart(HelloWorld(media=media), '/', conf)
