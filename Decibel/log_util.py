import logging

def logger():
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s %(name)s %(levelname)s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
    return logging
