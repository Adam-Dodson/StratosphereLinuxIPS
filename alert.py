#!/usr/bin/python -u
# This file is part of the Stratosphere Linux IPS
# See the file 'LICENSE' for copying permission.
#Author: Ondrej Lukas - ondrej.lukas95@gmail.com, lukasond@fel.cvut.cz

from datetime import datetime
from time import gmtime, strftime
from colors import *

class Alert(object):
    """docstring for Alert"""
    def __init__(self, time,source):
        self.time = time
        self.source = source
    def __str__(self):
        print "function print_alert() has to be implemented in derived class!"
        return  NotImplemented

class IpDetectionAlert(Alert):
    """docstring for IpDetectionAlert"""
    def __init__(self, time, source, score):
        super(IpDetectionAlert, self).__init__(time,source)
        self.score = score

    def __str__(self):
        return yellow('*detected with score {}\ttime: {}*'.format(self.score,self.time.strftime('%Y/%m/%d %H:%M:%S')))

class TupleDetectionAlert(object):
    """docstring for TupleDetectionAlert"""
    def __init__(self, time, source,model):
        super(TupleDetectionAlert, self).__init__(time,source)
        self.model = model