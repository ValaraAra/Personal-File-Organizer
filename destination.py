import os

from loguru import logger

class Destination():
    def __init__(self, name: str, path: str, extensions: list):
        self.name = name
        self.path = path
        self.extensions = extensions
        self.dirName = path.split('\\')[-1]
        self.checkDir()

    # Check to make sure the destination directory exists.
    def checkDir(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path, exist_ok=True)
            logger.log("SETUP", f"Created {self.dirName} Directory!\n")
