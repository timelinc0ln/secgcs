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
    import secgcs_pb2
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
    def __init__(self, zmq_filter, log=None):
        self.ctx = zmq.Context()
        self.sock = self.ctx.socket(zmq.SUB)
        self.sock.setsockopt(zmq.SUBSCRIBE, zmq_filter)
        self.log('created ZeroMQ subscribe socket', 'info')

    ## Connect to a ZeroMQ PUB server.
    #
    # @param host   [string] The FQDN or IP of the server
    # @param port   [string] The port binding for the server
    def connect(self, host='localhost', port='5555'):
        uri = 'tcp://%(host)s:%(port)s' % {'host': host,
                                           'port': port}
        self.sock.connect(uri)
        self.log('connected to server %(uri)s' % {'uri': uri}, 'info')

    ## Receive a message over the ZeroMQ socket.
    #
    # Receive one message from the PUB-SUB model, parse, and return.
    # TODO: Add code to de-serialize protobufs when .proto format is defined.
    #
    # @retval data  [string] The message content.
    def receive(self):
        msg = self.sock.recv()
        topic, data = msg.split()
        self.log('recieved message with topic %(topic)s and content %(data)s'
                 % {'topic': topic, 'data': data}, 'info')
        return data

    ## Wrapper for logging functionality.
    #
    # A wrapper to use the mplogger option if available; falls back to
    # using print() to stdout or stderr otherwise.
    #
    # @param msg    [string] The message to log
    # @param lvl    [string or int] The message log level
    def log(self, msg, lvl):
        if self.log is not None:
            self.log.putLog(lvl, msg)
        else:
            f = sys.stderr if lvl is 'error' else sys.stdout
            print(msg, file=f)
