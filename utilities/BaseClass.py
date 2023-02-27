import inspect
import logging

import pytest


@pytest.mark.usefixtures("Setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]  # will help you tell from which file this class is calling in log info
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler(
            'C:/Users/Cloud Analogy/PycharmProjects/pythonfolder/pythonE2E/Logs/logfiles.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger



