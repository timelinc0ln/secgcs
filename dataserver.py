#!/usr/bin/env python2
# -*- coding: utf-8 -*-
## @package dataserver
# Generate fake data for the UI.
#
from __future__ import print_function
from __future__ import unicode_literals
import argparse
import random
import time
try:
    import zmq
except ImportError:
    print('error: PyZMQ required', file=sys.stderr)
    print('exiting %s' % __file__, file=sys.stderr)
    exit(-1)

# Custom libs.
import messaging
import secgcs_pb2 as pb

def server(host='127.0.0.100', port='5555', verbose=False):
    # Set up ZeroMQ PUB server.
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    socket = 'tcp://%(host)s:%(port)s' % {'host': host, 'port': port}
    if verbose:
        print(socket)
    publisher.bind(socket)

    # Message topic is 'QGC'.
    topic = 'QGC'

    # Create Protocol Buffer message.
    msg = pb.QGCData()
    msg.msg_type = topic

    # Generate false data.
    while True:
        # Latitude
        msg.latitude = random.randint(-2**32, 2**32)
        # Longitude
        msg.longitude = random.randint(-2**32, 2**32)
        # Heading
        msg.heading = random.randint(0, 360)
        # Altitude
        msg.altitude = random.uniform(0, 400)
        # Serialize.
        msg_str = msg.SerializeToString()
        publisher.send(msg_str)
        if verbose:
            print('-----------------------')
            print('new set of fake data:')
            print('latitude: %d' % msg.latitude)
            print('longitude: %d' % msg.longitude)
            print('heading: %d' % msg.heading)
            print('altitude: %f' % msg.altitude)
        time.sleep(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--hostname', help='hostname',
                        type=str, default='127.0.0.1')
    parser.add_argument('-p', '--port', help='port', type=str, default='5555')
    parser.add_argument('-v', '--verbose', help='increase output verbosity',
                        action='store_true', default=False)
    args = parser.parse_args()
    server(host=args.hostname, port=args.port, verbose=args.verbose)
