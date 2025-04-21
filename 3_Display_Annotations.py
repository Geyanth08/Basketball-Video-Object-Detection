import os
import cv2
import random
import matplotlib.pyplot as plt

def get_annotations(original_img_file):
    annotations = []
    with open(original_img_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            values = line.strip().split()
            label = int(values[0])
            x_center, y_center, width, height = map(float, values[1:])
            annotations.append((label, x_center, y_center, width, height))
    return annotations

def put_annotations_in_image(image, annotations, label_names):
    h, w, _ = image.shape
    for annotation in annotations:
        label, x_center, y_center, width, height = annotation
        label_name = label_names[label]

        # Convert YOLO coordinates to pixel coordinates
        x1 = int((x_center - width / 2) * w)
        y1 = int((y_center - height / 2) * h)
        x2 = int((x_center + width / 2) * w)
        y2 = int((y_center + height / 2) * h)

        # Draw bounding box
        cv2.rectangle(image, (x1, y1), (x2, y2), (200, 0, 0), 2)

        # Display label
        cv2.putText(image, label_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 0, 0), 2, cv2.LINE_AA)
    return image

def display_random_images_mpl(folder_path, num_images, label_folder, label_names):
    # Get list of all image filenames in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
    if not image_files:
        print(f"No image files found in {folder_path}")
        return

    # Randomly select num_images
    random_images = random.sample(image_files, min(num_images, len(image_files)))

    # Create a subplot grid
    rows = (num_images + 3) // 4  # Adjusted to display num_images in a grid
    cols = min(num_images, 4)
    fig, axes = plt.subplots(rows, cols, figsize=(16, 4 * rows))
    axes = axes.flatten() # Flatten the axes array for easy indexing

    # Iterate through the randomly selected images and display them with annotations
    for i, image_file in enumerate(random_images):
        image_path = os.path.join(folder_path, image_file)
        label_file_base = os.path.splitext(image_file)[0] + '.txt'
        original_img_file = os.path.join(label_folder, label_file_base)

        if os.path.exists(original_img_file):
            try:
                img = cv2.imread(image_path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert BGR to RGB for matplotlib
                annotations = get_annotations(original_img_file)
                image_with_annotations = put_annotations_in_image(img.copy(), annotations, label_names)

                ax = axes[i]
                ax.imshow(image_with_annotations)
                ax.set_title(image_file)
                ax.axis('off') # Turn off axis labels and ticks

            except Exception as e:
                print(f"Error processing {image_file}: {e}")
        else:
            print(f"Annotation file not found for {image_file}")

    # Remove any unused subplots
    for j in range(len(random_images), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    IMAGE_FOLDER = "D:/M.Tech/2nd Sem/IVA_Lab/Basketball_detection/dataset/train/images"  # Replace with the path to your images folder
    LABEL_FOLDER = "D:/M.Tech/2nd Sem/IVA_Lab/Basketball_detection/dataset/train/labels"  # Replace with the path to your labels folder
    LABEL_NAMES = ["Maccabi player", "Real Madrid player", "ball", "referee"] # Ensure this matches your label indices
    NUM_DISPLAY = 4  # Number of random images to display

    display_random_images_mpl(IMAGE_FOLDER, NUM_DISPLAY, LABEL_FOLDER, LABEL_NAMES)