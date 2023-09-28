# Personal File Organizer

This python script organizes your Downloads and Desktop folders by file type.

## Requirements
```
Python 3.7+
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

## How it works

- Creates the Output folder and it's sub-folders if they don't already exist.
```
Output
    Images
    Audio
    Video
    Documents
    Archives
    Other
```
- Performs an initial sweep of your Downloads and Desktop folders, sorting files with supported extensions into their respective category in the Output folder.

- Actively monitors for new files, sorting them just like in the initial sweep.

## Logs
Logs are saved to `organizer-log.log` in the output folder.

```
[2023-09-27 19:29:11] INFO - Organizing Desktop & Downloads
[2023-09-27 19:29:11] INFO - Output: C:\Users\Valara\Desktop\Organizer Output

[2023-09-27 19:29:11] SUCCESS - Moved Image File: Silly Cat.png
[2023-09-27 19:29:11] SUCCESS - (C:\Users\Valara\Desktop\Silly Cat.png) -> (C:\Users\Valara\Desktop\Organizer Output\Images\Silly Cat.png)

[2023-09-27 19:29:11] SUCCESS - Moved Video File: Silly Cat Video.mp4
[2023-09-27 19:29:11] SUCCESS - (C:\Users\Valara\Downloads\Silly Cat Video.mp4) -> (C:\Users\Valara\Desktop\Organizer Output\Video\Silly Cat Video.mp4)

[2023-09-27 19:29:11] SUCCESS - Moved Document File: settings.txt
[2023-09-27 19:29:11] SUCCESS - (C:\Users\Valara\Desktop\settings.txt) -> (C:\Users\Valara\Desktop\Organizer Output\Documents\settings.txt)
```