import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from config import *

# Helper Functions
def getColoredText(text, color):
    return f"<{color}>{text}</{color}>"

def isDirectoryValid(path: Path):
    if path.exists() and path.is_dir():
        return True
    
    return False

def isFileValid(path: Path):
    if path.exists() and path.is_file():
        return True
    
    return False

def isFileIgnored(path: Path):
    if path.name in IGNORED_FILES:
        return True
    
    if path.suffix.lower() in IGNORED_EXTENSIONS:
        return True
    
    return False

def getUniqueFilePath(path: Path):
    newPath = path
    counter = 1
    
    while newPath.exists():
        newName = f"{path.stem}({counter}){path.suffix}"
        newPath = Path(path.parent, newName)
        counter += 1
    
    return newPath

def moveFile(path: Path, destination: Destination):
    if not isFileValid(path):
        logger.opt(colors=True).warning(f"File Invalid: {getColoredText(path.name, COLOR_FILE_NAME)} ({getColoredText(path, COLOR_FILE_PATH)})\n")
        return
    
    destination.checkDir()
    
    finalPath = getUniqueFilePath(Path(destination.path, path.name))
    
    try:
        shutil.move(path, finalPath)
    except OSError as error:
        fileStat = path.stat()
        if type(error) is PermissionError and fileStat.st_atime == fileStat.st_mtime:
            logger.opt(colors=True).log("IGNORED", f"File Being Created: {getColoredText(path.name, COLOR_FILE_NAME)} ({getColoredText(path, COLOR_FILE_PATH)})\n")
            return
        else:
            logger.opt(colors=True).error(f"Moving {destination.name} File: {getColoredText(path.name, COLOR_FILE_NAME)} ({getColoredText(path, COLOR_FILE_PATH)})")
            logger.opt(colors=True).error(f"({getColoredText(error, COLOR_ERROR)})\n")
            return
    
    logger.opt(colors=True).success(f"Moved {destination.name} File: {getColoredText(path.name, COLOR_FILE_NAME)}")
    logger.opt(colors=True).success(f"({getColoredText(path, COLOR_FILE_PATH)}) -> ({getColoredText(finalPath, COLOR_FILE_PATH)})\n")

def processFile(path: Path):
    if not isFileValid(path) or isFileIgnored(path):
        return
    
    for destination in DESTINATIONS:
        if path.suffix.lower() in destination.extensions:
            moveFile(path, destination)
            return
    
    logger.opt(colors=True).log("IGNORED", f"Unsupported Extension: {getColoredText(path.name, COLOR_FILE_NAME)} ({getColoredText(path, COLOR_FILE_PATH)})\n")

def sweepDirectories():
    logger.opt(colors=True).debug(f"<{COLOR_DEBUG}>Running Sweep</{COLOR_DEBUG}>\n")
    
    for directory in DIR_INPUTS:
        with os.scandir(directory) as entries:
            for entry in entries:
                processFile(Path(entry.path))
    
    logger.opt(colors=True).debug(f"<{COLOR_DEBUG}>Finished Sweep</{COLOR_DEBUG}>\n")

# Startup Log Message
logger.opt(colors=True).info(f"<{COLOR_START}>Organizing Folders</{COLOR_START}>")
logger.opt(colors=True).info(f"Output: {getColoredText(DIR_OUTPUT, COLOR_FILE_PATH)}\n")

# Ensure All Necessary Directories Are Valid
if not isDirectoryValid(DIR_OUTPUT):
    logger.opt(colors=True).error(f"Output Directory Invalid!\n")
    quit()

if len(DIR_INPUTS) < 1:
    logger.opt(colors=True).error(f"No Input Directories!\n")
    quit()

for directory in DIR_INPUTS:
    if not isDirectoryValid(directory):
        logger.opt(colors=True).error(f"Input Directory Invalid: ({getColoredText(directory, COLOR_ERROR)})\n")
        quit()

for destination in DESTINATIONS:
    if DIR_OUTPUT.samefile(destination.path):
        logger.opt(colors=True).error(f"An Input Directory Cannot Match An Output Destination!\n")
        quit()

# Initial File Sweep
sweepDirectories()

# Watchdog Event Handler
class EventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        processFile(Path(event.src_path))

# Watchdog Setup
if __name__ == "__main__":
    # Setup
    eventHandler = EventHandler()
    observers = []
    
    def observersAlive(observers):
        for observer in observers:
            if not observer.is_alive():
                return False
        
        return True
    
    # Start Watching (ignores sub-directories)
    for directory in DIR_INPUTS:
        observer = Observer()
        observer.schedule(eventHandler, directory, recursive=False)
        observer.start()
        observers.append(observer)
    
    logger.opt(colors=True).debug(f"<{COLOR_DEBUG}>Started Monitoring</{COLOR_DEBUG}>\n")
    
    # Handle Observers
    try:
        while observersAlive(observers):
            for observer in observers:
                observer.join(1)
    except KeyboardInterrupt as error:
        logger.opt(colors=True).info(f"<{COLOR_SHUTDOWN}>Shutting Down</{COLOR_SHUTDOWN}>\n")
    finally:
        for observer in observers:
            observer.stop()
        for observer in observers:
            observer.join()

quit()
