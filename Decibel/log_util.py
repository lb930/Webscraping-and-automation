import logging

def logger():
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                              datefmt='%H:%M:%S', level=logging.INFO)
    return logging