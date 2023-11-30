import os, shutil

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
files_on_desktop = os.listdir(desktop_path)

image_extensions = [".PNG", ".JPG", ".HEIC", ".JPEG",".jpeg", ".gif", ".png"]
document_extensions = [".doc", ".docx", ".txt", ".pdf", ".epub"]
video_extensions = [".mp4", ".wav", ".mov"]
song_extensions = [".mp3"]


image_files = [file for file in files_on_desktop if os.path.splitext(file)[1] in image_extensions]
doc_files = [file for file in files_on_desktop if os.path.splitext(file)[1] in document_extensions]
video_files = [file for file in files_on_desktop if os.path.splitext(file)[1] in video_extensions]
music_files = [file for file in files_on_desktop if os.path.splitext(file)[1] in song_extensions]


images_folder = os.path.join(desktop_path, "Screenshots")
documents_folder = os.path.join(desktop_path, "Documents")
videos_folder = os.path.join(desktop_path, "Videos")
music_folder = os.path.join(desktop_path, "Music")

create_folder(images_folder)
create_folder(documents_folder)
create_folder(videos_folder)
create_folder(music_folder)

def move_file(src, dst):
    if os.path.exists(dst):
        base, ext = os.path.splitext(dst)
        counter = 1
        while os.path.exists(dst):
            dst = f"{base}_{counter}{ext}"
            counter+=1

    shutil.move(src, dst)

for file in image_files:
    shutil.move(os.path.join(desktop_path, file), os.path.join(images_folder, file))

for file in doc_files:
    shutil.move(os.path.join(desktop_path, file), os.path.join(documents_folder, file))

for file in video_files:
    shutil.move(os.path.join(desktop_path, file), os.path.join(videos_folder, file))

for file in music_files:
    shutil.move(os.path.join(desktop_path, file), os.path.join(music_folder, file))
