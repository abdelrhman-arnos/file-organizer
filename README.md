# File Organizer Script

## Description

This Python script automates the organization of files within a specified directory. It scans the directory for files and sorts them into folders based on their file types (extensions). This helps keep your workspace clean and makes it easier to find files.

## Features

- **Automatic Folder Creation**: Creates folders for each file type if they don't already exist.
- **File Sorting**: Moves files into their respective folders based on extension.
- **Easy to Use**: Simply place the script in the directory and run it.

## Requirements

- Python 3.x

## Usage

1. **Place the Script**: Copy `organize_files.py` into the directory you want to organize.

2. **Run the Script**:

   Open a terminal, navigate to the directory, and execute:

   ```bash
   python organize_files.py

3. **Result**:

- Files will be moved into folders named after their file extensions.
- Files without an extension will be moved to a folder named no_extension.

## Example

Before running the script:
```
your_directory/
├── organize_files.py
├── document1.pdf
├── image1.png
├── script1.py
├── notes.txt
```

After running the script:
```
your_directory/
├── organize_files.py
├── pdf/
│   └── document1.pdf
├── png/
│   └── image1.png
├── py/
│   └── script1.py
├── txt/
    └── notes.txt
```

## Notes

The script skips directories and only processes files.
Backup important data before running the script to prevent accidental data loss.
Ensure you have the necessary permissions to read and write files in the directory.
