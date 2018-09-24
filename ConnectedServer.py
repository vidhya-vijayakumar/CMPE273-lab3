from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

# Here's a UDP version of the simplest possible protocol
class Helloer1(DatagramProtocol):
    def datagramReceived(self, datagram, address):
        self.transport.write(datagram, address)

reactor.listenUDP(3011, Helloer1())
reactor.run()