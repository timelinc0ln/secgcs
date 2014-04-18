#!/usr/bin/env python2
# -*- coding: utf-8 -*-
## @package mplogging
# Documentation for the mplogging module
#

# Standard library modules
import logging
import logging.handlers
import multiprocessing as mp

# Definitions
LOGPATH = ''
LOGNAME = 'secgcs.log'
LOGLEVEL = logging.DEBUG

# Logging levels
DEBUG = logging.DEBUG           # 10
INFO = logging.INFO             # 20
WARNING = logging.WARNING       # 30
ERROR = logging.ERROR           # 40
CRITICAL = logging.CRITICAL     # 50


## Logging queue
def logQueue():
    return mp.Queue()


## Root logger process
class RootLog(mp.Process):

    ## Root logger process constructor.
    def __init__(self, logQueue):
        mp.Process.__init__(self)
        self.logQueue = logQueue
        self.daemon = True

    ## Root logger configurer
    def rootLogCfg(self):
        root = logging.getLogger()
        h = logging.handlers.TimedRotatingFileHandler(LOGPATH + LOGNAME,
                                                      'midnight', 1)
        f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
        h.setFormatter(f)
        root.addHandler(h)

    def run(self):
        self.rootLogCfg()
        while True:
            try:
                record = self.logQueue.get()
                if record is None:  # We send this as a sentinel to tell the listener to quit.
                    break
                logger = logging.getLogger(record.name)
                logger.handle(record)  # No level or filter logic applied - just do it!
            except (KeyboardInterrupt, SystemExit):
                pass
            except:
                import sys
                import traceback
                print >> sys.stderr, 'Root logging error:'
                traceback.print_exc(file=sys.stderr)


## Logging queue handler.
class QueueHandler(logging.Handler):

    ## Logging queue handler constructor.
    #
    # @param self Queue handler pointer.
    # @param queue Shared queue object for putting logs.
    def __init__(self, logQueue):
        logging.Handler.__init__(self)
        self.logQueue = logQueue

    ## Writes a log record to the queue
    def emit(self, record):
        try:
            ei = record.exc_info
            if ei:
                dummy = self.format(record)  # just to get traceback text into record.exc_text
                record.exc_info = None  # not needed any more
            self.logQueue.put_nowait(record)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


## Working process logging object
class ProcLog(object):
    ## Working process logging object constructor.
    #
    # @param self Logging object pointer.
    # @param logQueue Shared queue object for putting logs.
    def __init__(self, logQueue, logName):
        self.logQueue = logQueue
        self.logName = logName
        h = QueueHandler(self.logQueue)
        self.root = logging.getLogger()
        self.root.addHandler(h)
        self.root.setLevel(LOGLEVEL)
        self.logger = logging.getLogger(self.logName)

    ## Put log onto logging queue method.
    #
    # @param self Logging object pointer.
    # @param logName Logging name to use
    # @param level Level of message to put.
    # @param message Message to put.
    def putLog(self, level, message):
        levels = {
            'debug': DEBUG,
            'info': INFO,
            'warning': WARNING,
            'error': ERROR,
            'critical': CRITICAL,
        }
        if type(level) is str:
            level = levels[level.lower()]
        self.logger.log(level, message)

    ## Set minimum level for actually putting on the queue
    #
    # @param self Logging object pointer.
    # @param logLevel Logging level to set as minumum.
    def setLevel(self, logLevel):
        self.root.setLevel(logLevel)

    def setName(self, logName):
        self.logName = logName
        del self.logger
        self.logger = logging.getLogger(self.logName)
