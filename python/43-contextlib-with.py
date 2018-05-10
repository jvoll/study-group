from contextlib import contextmanager
import logging

@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

with log_level(logging.DEBUG, 'my-log') as logger:
    print(logger.getEffectiveLevel())
    # logger.setLevel(logging.DEBUG)
    logger.debug('This is my message!')
    logging.debug('This will not print -- only set log level to DEBUG on logger not logging')

logger = logging.getLogger('my-log')
logger.debug('Debug will not print')
logger.error('Error will print')


# @study-group...why won't any debug print?!?!
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
