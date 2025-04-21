import os
from ultralytics import YOLO
from vidgear.gears import CamGear
import cv2
import random  # For generating random colors

# Test URL (replace with your actual test video URL)
test_url = "https://youtu.be/C9XBFSOuamA?si=MVAQczEwnWWfgj8o"

# Load the model
model_path_base = "D:\\M.Tech\\2nd Sem\\IVA_Lab\\Basketball_detection"
model_folder = "small-Model3"
weights_folder = "weights"
model_file = "best.pt"
model_path = os.path.join(model_path_base, model_folder, weights_folder, model_file)
print(f"Attempting to load model from: {model_path}")  # Add this line

model = YOLO(model_path)
threshold = 0.25

# Desired width and height for the output window
output_width = 800
output_height = 600

# Create a dictionary to store colors for each class
class_colors = {}

def get_color(class_id):
    """Generates a unique color for each class ID."""
    if class_id not in class_colors:
        # Generate a random BGR color (OpenCV uses BGR)
        blue = random.randint(0, 255)
        green = random.randint(0, 255)
        red = random.randint(0, 255)
        class_colors[class_id] = (blue, green, red)
    return class_colors[class_id]

# Path to our YouTube video file
stream = CamGear(source=test_url, stream_mode=True, logging=True).start()

while True:
    frame = stream.read()
    if frame is None:
        break

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        if score > threshold:
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)
            color = get_color(int(class_id))  # Get a unique color for the class
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, results.names[int(class_id)].upper(), (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    # Resize the frame before displaying
    resized_frame = cv2.resize(frame, (output_width, output_height))

    cv2.imshow("img", resized_frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
stream.stop()