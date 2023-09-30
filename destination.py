import os

from pathlib import Path
from loguru import logger

class Destination():
    def __init__(self, name: str, path: Path, extensions: list):
        self.name = name
        self.path = path
        self.extensions = extensions

    # Check to make sure the destination directory exists.
    def checkDir(self):
        if not self.path.exists():
            os.makedirs(self.path, exist_ok=True)
            logger.log("SETUP", f"Created {self.path.parent.stem} Directory!\n")
