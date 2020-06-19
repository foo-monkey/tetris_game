import os
import logging
from logging.handlers import RotatingFileHandler

import datetime,time
#need to add config file.
#from configUtils import config


#### Variables declaration
logfile = config.get("Global" , "LOG_FILE")
#logname = 'Aggregate process'
logformat = '%(asctime)s %(levelname)-8s %(process)s %(message)s'
logformat = "%(asctime)s,%(msecs)d %(name)s (%(process)s) 1 %(levelname)s: %(message)s"
frmDate = "%d-%m-%y %H:%M:%S"

global log

#############################################################################
# create logger with 'Aggregate process'
log = logging.getLogger()
log.setLevel(logging.DEBUG)
#log.setLevel(logging.ERROR)

# create file handler which logs even debug messages
fh = RotatingFileHandler(logfile, mode='a', maxBytes=10240000, backupCount=2)
fh.setLevel(logging.DEBUG)
#fh.setLevel(logging.ERROR)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter(logformat,frmDate)
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
log.addHandler(fh)
log.addHandler(ch)

# log.debug("test - {}".format(__name__))