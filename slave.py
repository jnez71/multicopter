from __future__ import division

import time

from twisted.internet import defer, reactor

import deferral
import xbee


@defer.inlineCallbacks
def main():
    xb = yield xbee.XBee(reactor, '/dev/ttyO0', 230400)
    
    while True:
        packet, = yield xb.packet_received.get_deferred()
        print packet['data']
deferral.launch_main(main)
