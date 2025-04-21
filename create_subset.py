import os
import shutil
import random

def move_image_subset(source_folder, destination_folder, num_images):
    """
    Moves a subset of random images from a source folder to a new destination folder.

    Args:
        source_folder (str): Path to the folder containing the original images.
        destination_folder (str): Path to the folder where the subset will be moved.
        num_images (int): The number of random images to select and move.
    """
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: '{destination_folder}'")
    elif os.listdir(destination_folder):
        print(f"Warning: Destination folder '{destination_folder}' already exists and is not empty. New images will be added.")

    all_images = [f for f in os.listdir(source_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    if not all_images:
        print(f"Warning: No image files found in the source folder '{source_folder}'.")
        return

    num_available_images = len(all_images)
    num_to_select = min(num_images, num_available_images)

    if num_to_select == 0:
        print("No images selected to move.")
        return

    random_images = random.sample(all_images, num_to_select)

    print(f"Moving {num_to_select} random images...")

    for image_name in random_images:
        source_path = os.path.join(source_folder, image_name)
        destination_path = os.path.join(destination_folder, image_name)
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved: '{image_name}' to '{destination_folder}'")
        except Exception as e:
            print(f"Error moving '{image_name}': {e}")

    print("Image moving complete.")

if __name__ == "__main__":
    source_directory = "D:/M.Tech/2nd Sem/IVA_Lab/Basketball_detection/train_images/combined_images"  # Replace with the actual path to your source folder
    destination_directory = "D:/M.Tech/2nd Sem/IVA_Lab/Basketball_detection/train_images/subset"  # Replace with the desired path for the new subset folder
    number_of_images = 2000  # Specify the number of images you want to move to the subset

    move_image_subset(source_directory, destination_directory, number_of_images)