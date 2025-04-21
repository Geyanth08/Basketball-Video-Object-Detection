import os
import shutil

# Define the paths to your source folders and the destination folder
video_1_folder = r"D:/M.Tech/2nd Sem/IVA_Lab/Basketball_detection/train_images/video_1"
video_2_folder = r"D:/M.Tech/2nd Sem/IVA_Lab/Basketball_detection/train_images/video_2"
combined_folder = r"D:/M.Tech/2nd Sem/IVA_Lab/Basketball_detection/train_images/combined_images"

# Create the destination folder if it doesn't exist
os.makedirs(combined_folder, exist_ok=True)

# Function to copy images from a source folder to the combined folder
def copy_images(src_folder, dest_folder):
    for filename in os.listdir(src_folder):
        src_file = os.path.join(src_folder, filename)
        if os.path.isfile(src_file):
            dest_file = os.path.join(dest_folder, filename)
            # Check if the file already exists in the destination folder
            if not os.path.exists(dest_file):
                shutil.copy2(src_file, dest_folder)
            else:
                print(f"Skipping {filename}, already exists in the destination.")

# Copy images from both video folders to the combined folder
copy_images(video_1_folder, combined_folder)
copy_images(video_2_folder, combined_folder)

print(f"Images from '{video_1_folder}' and '{video_2_folder}' have been combined into '{combined_folder}'.")
