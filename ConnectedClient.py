from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def startProtocol(self):
        host = "127.0.0.1"
        port = 3011
        self.transport.connect('127.0.0.1', 3011)
        print("now we can only send to host %s port %d" % (host, port))
        self.transport.write(b'Hello World')

    def datagramReceived(self, datagram, host):
        print('Datagram received: ', repr(datagram))

    def connectionRefused(self):
        print("No one listening")

reactor.listenUDP(0, Helloer())
reactor.run()