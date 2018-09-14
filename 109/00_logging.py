import logging

#simple logging

##logging.basicConfig(level=logging.DEBUG)
##logging.basicConfig(level=logging.DEBUG, format='%(levelname)s  %(asctime)s  %(message)s')
##logging.basicConfig(level=logging.DEBUG, filename='test.log', format='%(levelname)s  %(asctime)s  %(message)s')

logging.debug("hi this is simple logging! (debug)")
logging.info("hi this is simple logging! (info)")
logging.warning("hi this is simple logging! (warning)")
logging.error("hi this is simple logging! (error)")

