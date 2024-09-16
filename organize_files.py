import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        # Skip directories and the script file itself
        if filename == os.path.basename(__file__) or os.path.isdir(os.path.join(directory, filename)):
            continue

        filepath = os.path.join(directory, filename)
        file_extension = os.path.splitext(filename)[1][1:].lower()

        if file_extension == '':
            file_extension = 'no_extension'

        folder_path = os.path.join(directory, file_extension)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.move(filepath, os.path.join(folder_path, filename))

    print("Files have been organized.")

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    organize_files(current_directory)
