#!/usr/bin/env python2
# -*- coding: utf-8 -*-
## @package messaging
# Messaging functions for communicating with QGroundControl
# @author Joshua Harris <joshua.a.harris@tamu.edu>
from __future__ import print_function
from __future__ import unicode_literals
import sys
# Custom libraries.
try:
    import zmq
except ImportError:
    print('error: PyZMQ required', file=sys.stderr)
    print('exiting %s' % __file__, file=sys.stderr)
    exit(-1)
try:
    import secgcs_pb2 as pb
except ImportError:
    print('error: protocol buffer module not found', file=sys.stderr)
    print('exiting %(file)s' % {'file': __file__}, file=sys.stderr)
    exit(-1)


## Class to handle messaging with QGroundControl using ZeroMQ.
#
# The ZMQMessageHandler class is a wrapper for the PyZMQ API to create
# a subscribe socket for receiving updates from a 'server' running in
# QGroundControl.
class ZMQMessageHandler(object):

    ## Constructor for ZMQMessageHandler class.
    #
    # Creates and initializes a ZMQ SUB socket.
    #
    # @param zmq_filter [string] Topic filter for ZeroMQ
    # @param log        [object] Pointer to the mplogger instance
    def __init__(self, zmq_filter='\x0A\x03\x51\x47\x43', log_target=None):
        self.log_target = log_target
        self.ctx = zmq.Context()
        self.sock = self.ctx.socket(zmq.SUB)
        self.sock.setsockopt_string(zmq.SUBSCRIBE, zmq_filter)
        self.log('created ZeroMQ subscribe socket', 'info')
        # Create protobuf message object.
        self.QGCData = pb.QGCData()

    ## Connect to a ZeroMQ PUB server.
    #
    # @param host   [string] The FQDN or IP of the server
    # @param port   [string] The port binding for the server
    def connect(self, host='127.0.0.100', port='5555'):
        uri = 'tcp://%(host)s:%(port)s' % {'host': host,
                                           'port': port}
        self.sock.connect(uri)
        self.log('connected to server %(uri)s' % {'uri': uri}, 'info')

    ## Receive a message over the ZeroMQ socket.
    #
    # Receive one message from the PUB-SUB model, parse, and return.
    # The data is serialized using Google protocol buffers, de-serialized,
    # and then packed into a dict for easy access in Python.
    #
    # @retval data  [string] The message content.
    def receive(self, verbose=False):
        msg = self.sock.recv()
        self.QGCData.ParseFromString(msg)
        # We will represent this data as a dict.
        data = {
            'latitude': self.QGCData.latitude,
            'longitude': self.QGCData.longitude,
            'altitude': self.QGCData.altitude,
            'heading': self.QGCData.heading
        }
        if verbose:
            print('------------------')
            print('recieved message')
            print('type: %s' % self.QGCData.msg_type)
            print('latitude: %d' % self.QGCData.latitude)
            print('longitude: %d' % self.QGCData.longitude)
            print('heading: %d' % self.QGCData.heading)
            print('altitude: %f' % self.QGCData.altitude)
        return data

    ## Wrapper for logging functionality.
    #
    # A wrapper to use the mplogger option if available; falls back to
    # using print() to stdout or stderr otherwise.
    #
    # @param msg    [string] The message to log
    # @param lvl    [string or int] The message log level
    def log(self, msg, lvl):
        if self.log_target is not None:
            self.log_target.putLog(lvl, msg)
        else:
            f = sys.stderr if lvl is 'error' else sys.stdout
            print(msg, file=f)


## Function to test data link.
def test():
    MsgHandler = ZMQMessageHandler()
    MsgHandler.connect(host='127.0.0.100')
    while True:
        MsgHandler.receive(verbose=True)


if __name__ == '__main__':
    test()
