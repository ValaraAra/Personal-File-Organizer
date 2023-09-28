import os
import shutil
import itertools

from loguru import logger

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from config import *

# Helper Functions
def getColoredText(text, color):
    return f"<{color}>{text}</{color}>"

def isFileValid(path):
    if os.path.exists(path) and os.path.isfile(path):
        return True
    
    return False

def isFileIgnored(name):
    if name in IGNORED_FILES:
        return True
    
    extension = os.path.splitext(name)[1].lower()
    if extension in IGNORED_EXTENSIONS:
        return True
    
    return False

def getUniqueFileName(name, destination_path):
    filename, extension = os.path.splitext(name)
    counter = 1
    
    while os.path.exists(os.path.join(destination_path, name)):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    
    return name

def moveFile(path, name: str, destination: Destination):
    if not isFileValid(path):
        logger.opt(colors=True).warning(f"File Invalid: {getColoredText(name, COLOR_FILE_NAME)} ({getColoredText(path, COLOR_FILE_PATH)})\n")
        return
    
    destinationPath = destination.path
    finalPath = os.path.join(destinationPath, name)
    
    if os.path.exists(finalPath):
        finalPath = os.path.join(destinationPath, getUniqueFileName(name, destinationPath))
    
    destination.checkDir()
    
    try:
        shutil.move(path, finalPath)
    except OSError as error:
        fileStat = os.stat(path)
        if type(error) is PermissionError and fileStat.st_atime == fileStat.st_mtime:
            logger.opt(colors=True).log("IGNORED", f"File Being Created: {getColoredText(name, COLOR_FILE_NAME)} ({getColoredText(path, COLOR_FILE_PATH)})\n")
            return
        else:
            logger.opt(colors=True).error(f"Moving {destination.name} File: {getColoredText(name, COLOR_FILE_NAME)} ({getColoredText(path, COLOR_FILE_PATH)})")
            logger.opt(colors=True).error(f"({getColoredText(error, COLOR_ERROR)})\n")
            return
    
    logger.opt(colors=True).success(f"Moved {destination.name} File: {getColoredText(name, COLOR_FILE_NAME)}")
    logger.opt(colors=True).success(f"({getColoredText(path, COLOR_FILE_PATH)}) -> ({getColoredText(finalPath, COLOR_FILE_PATH)})\n")

def processFile(path, name: str):
    if not isFileValid(path) or isFileIgnored(name):
        return
    
    extension = os.path.splitext(name)[1].lower()
    
    for destination in DESTINATIONS:
        if extension in destination.extensions:
            moveFile(path, name, destination)
            return
    
    logger.opt(colors=True).log("IGNORED", f"Unsupported Extension: {getColoredText(name, COLOR_FILE_NAME)} ({getColoredText(path, COLOR_FILE_PATH)})\n")

def sweepDirectories():
    with os.scandir(DIR_DOWNLOADS) as downloadsEntries, os.scandir(DIR_DESKTOP) as desktopEntries:
        logger.opt(colors=True).debug(f"<{COLOR_DEBUG}>Running Sweep</{COLOR_DEBUG}>\n")
        
        for entry in itertools.chain(downloadsEntries, desktopEntries):
            processFile(entry.path, entry.name)
        
        logger.opt(colors=True).debug(f"<{COLOR_DEBUG}>Finished Sweep</{COLOR_DEBUG}>\n")

# Startup Log Message
logger.opt(colors=True).info(f"<{COLOR_START}>Organizing Desktop & Downloads</{COLOR_START}>")
logger.opt(colors=True).info(f"Output: {getColoredText(DIR_OUTPUT, COLOR_FILE_PATH)}\n")

# Initial File Sweep
sweepDirectories()

# Watchdog Event Handler
class EventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        path = event.src_path
        processFile(path, os.path.basename(path))

# Watchdog Setup
if __name__ == "__main__":
    # The Event Handler
    eventHandler = EventHandler()
    
    # Start Watching Downloads & Desktop (ignores sub-directories)
    downloadsObserver = Observer()
    downloadsObserver.schedule(eventHandler, DIR_DOWNLOADS, recursive=False)
    downloadsObserver.start()
    
    desktopObserver = Observer()
    desktopObserver.schedule(eventHandler, DIR_DESKTOP, recursive=False)
    desktopObserver.start()
    
    logger.opt(colors=True).debug(f"<{COLOR_DEBUG}>Started Monitoring</{COLOR_DEBUG}>\n")
    
    # Handle Both Observers
    try:
        while downloadsObserver.is_alive() and desktopObserver.is_alive():
            downloadsObserver.join(1)
            desktopObserver.join(1)
    except KeyboardInterrupt as error:
        logger.opt(colors=True).info(f"<{COLOR_SHUTDOWN}>Shutting Down</{COLOR_SHUTDOWN}>\n")
    finally:
        downloadsObserver.stop()
        desktopObserver.stop()
        
        downloadsObserver.join()
        desktopObserver.join()

quit()
