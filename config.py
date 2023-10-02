import sys

from pathlib import Path
from destination import Destination

from loguru import logger

# Directory Setup
DIR_BASE = Path.home()
DIR_OUTPUT = Path(DIR_BASE, 'Desktop', 'Organizer Output')
DIR_INPUTS = [Path(DIR_BASE, 'Downloads'), Path(DIR_BASE, 'Desktop')]

# Log File
LOG_LEVEL = "INFO"
LOG_PATH = Path(DIR_OUTPUT, 'organizer-log.log')

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
logger.add(sys.stdout, level=LOG_LEVEL, format="[<light-magenta>{time:ddd hh:mm:ss A}</light-magenta>] <level>{level}</level> - {message}")
logger.add(LOG_PATH, delay=True, rotation="10 MB", retention="30 days", format="[{time:YYYY-MM-DD HH:mm:ss.SSS}] {level} - {message}")

# Destinations
DESTINATION_OUTPUT = Destination("Output", DIR_OUTPUT, None) # This is really only used to log the creation of the base Output folder
DESTINATION_IMAGE = Destination("Image", Path(DIR_OUTPUT, 'Images'), EXTENSIONS_IMAGE)
DESTINATION_AUDIO = Destination("Audio", Path(DIR_OUTPUT, 'Audio'), EXTENSIONS_AUDIO)
DESTINATION_VIDEO = Destination("Video", Path(DIR_OUTPUT, 'Video'), EXTENSIONS_VIDEO)
DESTINATION_DOCUMENT = Destination("Document", Path(DIR_OUTPUT, 'Documents'), EXTENSIONS_DOCUMENT)
DESTINATION_ARCHIVE = Destination("Archive", Path(DIR_OUTPUT, 'Archives'), EXTENSIONS_ARCHIVE)
DESTINATION_OTHER = Destination("Other", Path(DIR_OUTPUT, 'Other'), EXTENSIONS_OTHER)

DESTINATIONS = [DESTINATION_IMAGE, DESTINATION_AUDIO, DESTINATION_VIDEO,
    DESTINATION_DOCUMENT, DESTINATION_ARCHIVE, DESTINATION_OTHER]