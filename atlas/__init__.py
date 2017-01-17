import logging
import requests

# using SSL w/o certificate validation
requests.packages.urllib3.disable_warnings()

# loggers.
logging.basicConfig(level=logging.DEBUG)

# specific loggers
logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('httpstream').setLevel(logging.WARNING)
