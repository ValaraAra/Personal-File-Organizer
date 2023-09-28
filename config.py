import os
import sys

from loguru import logger
from destination import Destination

# Directory Setup
DIR_BASE = os.path.expanduser('~')
DIR_OUTPUT = f"{DIR_BASE}\Desktop\Organizer Output"
DIR_DOWNLOADS = f"{DIR_BASE}\Downloads"
DIR_DESKTOP = f"{DIR_BASE}\Desktop"

# Log File
LOG_PATH = f"{os.path.join(DIR_OUTPUT, 'organizer-log.log')}"

# Supported File Extensions
EXTENSIONS_IMAGE = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".pjpeg", ".pjg",
    ".png", ".apng", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2",
    ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2",
    ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps",
    ".ico", ".cur", ".avif",]
EXTENSIONS_AUDIO = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac",]
EXTENSIONS_VIDEO = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd",]
EXTENSIONS_DOCUMENT = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".txt",
    ".html", ".htm", ".ppt", ".pptx", ".odp", ".key", ".cfg", ".ini", ".ttf",]
EXTENSIONS_ARCHIVE = [".rar", ".zip", ".7z", ".tar", ".iso", ".pea",]
EXTENSIONS_OTHER = [".exe", ".jar", ".apk",]

# Ignored Files / Extensions
IGNORED_EXTENSIONS = [".tmp", ".temp", ".lck", ".lock", ".crdownload", ".part", ".lnk",]
IGNORED_FILES = ["desktop.ini",]

# Colors
COLOR_ERROR = "red"
COLOR_DEBUG = "light-blue"
COLOR_START = "light-green"
COLOR_SHUTDOWN = "light-red"
COLOR_FILE_NAME = "light-cyan"
COLOR_FILE_PATH = "light-black"

# Logging Setup
logger.remove()
logger.level("SETUP", no=10, color="<light-yellow>")
logger.level("IGNORED", no=15, color="<light-yellow>")
logger.add(sys.stdout, level="INFO", format="[<light-magenta>{time:ddd hh:mm:ss A}</light-magenta>] <level>{level}</level> - {message}")
logger.add(LOG_PATH, delay=True, rotation="10 MB", retention="30 days", format="[{time:YYYY-MM-DD HH:mm:ss.SSS}] {level} - {message}")

# Destinations
DESTINATION_OUTPUT = Destination("Output", DIR_OUTPUT, None) # This is really only used to log the creation of the base Output folder
DESTINATION_IMAGE = Destination("Image", f"{DIR_OUTPUT}\Images", EXTENSIONS_IMAGE)
DESTINATION_AUDIO = Destination("Audio", f"{DIR_OUTPUT}\Audio", EXTENSIONS_AUDIO)
DESTINATION_VIDEO = Destination("Video", f"{DIR_OUTPUT}\Video", EXTENSIONS_VIDEO)
DESTINATION_DOCUMENT = Destination("Document", f"{DIR_OUTPUT}\Documents", EXTENSIONS_DOCUMENT)
DESTINATION_ARCHIVE = Destination("Archive", f"{DIR_OUTPUT}\Archives", EXTENSIONS_ARCHIVE)
DESTINATION_OTHER = Destination("Other", f"{DIR_OUTPUT}\Other", EXTENSIONS_OTHER)

DESTINATIONS = [DESTINATION_IMAGE, DESTINATION_AUDIO, DESTINATION_VIDEO,
    DESTINATION_DOCUMENT, DESTINATION_ARCHIVE, DESTINATION_OTHER]