import os
import shutil

source_folder = input("Enter the folder path to organize: ")

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Code': ['.py', '.cpp', '.c', '.js', '.java'],
    'Others': []
}

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder, extensions in file_types.items():
            if file_ext in extensions:
                dest_folder = os.path.join(source_folder, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                moved = True
                break

        if not moved:
            others_folder = os.path.join(source_folder, 'Others')
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))

print("✅ Files organized successfully!")
