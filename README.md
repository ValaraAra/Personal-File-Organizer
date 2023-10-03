# Personal File Organizer
[![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/) [![](https://img.shields.io/badge/code_style-black-black)](https://github.com/psf/black) [![](https://img.shields.io/github/license/ValaraAra/Personal-File-Organizer.svg)](https://github.com/ValaraAra/Personal-File-Organizer/blob/master/LICENSE.md)

This python script monitors and organizes your Downloads and Desktop directories by file type.

(While organizing the Downloads and Desktop directories is the default, it can easily be used with any directories)

## Requirements
```
Watchdog
Loguru
```

## Get Started

1. Clone the repo or download the zip

2. Navigate to the folder in terminal
```
cd "path-to-folder-here"
```

3. Install requirements using pip or conda
```
pip install -r requirements.txt
```
```
conda install --file requirements.txt
```

4. Start the script
```
python main.py
```

## Launch Arguments
- Output Path (-o, --output)
```
python main.py --output "output-path-here"
```

- Input Path(s) (-i, --input)
```
python main.py --input "input-path-here"
```
```
python main.py --input "input-1-here" "input-2-here" "input-3-here"
```

- Console Log Level (-l, --level)
```
DEBUG, INFO, WARNING
```
```
python main.py --level "log-level-here"
```

- Example Usage (defaults, minus desktop input)
```
python main.py --output "C:\Users\Valara\Desktop\Organizer Output" --input "C:\Users\Valara\Downloads" --level "INFO"
```

## How it works

- Creates the Output directory and it's sub-directories if they don't already exist.
```
Output
    Images
    Audio
    Video
    Documents
    Archives
    Other
```
- Performs an initial sweep of your Input directories, sorting files with supported extensions into their respective category in the Output directory.

- Actively monitors for new files, sorting them just like in the initial sweep.

## Logs
Logs are saved to `organizer-log.log` in the output folder.

```
[2023-09-27 19:29:11] INFO - Organizing Folders
[2023-09-27 19:29:11] INFO - Output: C:\Users\Valara\Desktop\Organizer Output

[2023-09-27 19:29:11] SUCCESS - Moved Image File: Silly Cat.png
[2023-09-27 19:29:11] SUCCESS - (C:\Users\Valara\Desktop\Silly Cat.png) -> (C:\Users\Valara\Desktop\Organizer Output\Images\Silly Cat.png)

[2023-09-27 19:29:11] SUCCESS - Moved Video File: Silly Cat Video.mp4
[2023-09-27 19:29:11] SUCCESS - (C:\Users\Valara\Downloads\Silly Cat Video.mp4) -> (C:\Users\Valara\Desktop\Organizer Output\Video\Silly Cat Video.mp4)

[2023-09-27 19:29:11] SUCCESS - Moved Document File: settings.txt
[2023-09-27 19:29:11] SUCCESS - (C:\Users\Valara\Desktop\settings.txt) -> (C:\Users\Valara\Desktop\Organizer Output\Documents\settings.txt)
```