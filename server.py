
# Basic services
from spyne import Application, rpc, Service, Integer, Float

# Communication protocol
from spyne.protocol.soap import Soap11

# new server and server config
import logging
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class Calculator(Service):
    @rpc(Integer, Integer, _returns=Integer)
    def sum(ctx, first, second):
        return first + second

    @rpc(Integer, Integer, _returns=Integer)
    def sub(ctx, first, second):
        return first - second

    @rpc(Integer, Integer, _returns=Integer)
    def mul(ctx, first, second):
        return first * second

    @rpc(Integer, Integer, _returns=Float)
    def div(ctx, first, second):
        return first / second

# SOAP config
# server receives a envelope SOAP 1.1
# server responses a envelop SOAP 1.1
application = Application([Calculator], 'spyne.project_DS.SOAP',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    
    # server config
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    # server init
    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()