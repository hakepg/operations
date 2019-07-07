import logging

# logging.debug('Hello Python')
# logging.info('Hell/o Python')
# logging.warning('Hello Python')
# logging.error('Hell/o Python')
# logging.critical('Hello Python')



# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will get logged')



# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#
# logging.warning('This will get logged to a file')
#
#
#
# logging.basicConfig(filename='app.log', filemode='a',format='%(process)d-%(levelname)s-%(message)s',level=logging.WARNING)
# logging.warning('This is a Warning')
# logging.warning('This will get logged to a file')



# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Admin logged out')
logging.basicConfig(format='%(asctime)s - %(message)s')
logging.info('Admin logged in')