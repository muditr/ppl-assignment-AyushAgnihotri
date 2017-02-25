import logging

def log_maker(write) :
	logging.basicConfig(filename='log_text.log',datefmt='%d/%m/%Y %I:%M:%S %p',format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',level=logging.DEBUG,filemode='w')
	logging.info(write)