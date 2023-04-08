import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='.\\logs\\automation.log', format='%(asctime)s: %(levelname)s: %(message)s', 
        dateformat='%m/%d/%Y %I:%M:%S %p ')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger