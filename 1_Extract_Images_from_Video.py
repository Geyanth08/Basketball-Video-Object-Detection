from vidgear.gears import CamGear
import cv2
import os

train_urls = [
    "https://youtu.be/32bsPfx1kmY?si=p0iwTufEBoztdckQ",
    "https://youtu.be/QxzdEivMbvE?si=pMFhuHBNaYC-6vK6"
]

output_base_path = "train_images"
os.makedirs(output_base_path, exist_ok=True)

for i, url in enumerate(train_urls):
    video_name = f"video_{i+1}"
    output_path_video = os.path.join(output_base_path, video_name)
    os.makedirs(output_path_video, exist_ok=True)

    try:
        # Initialize CamGear stream
        stream = CamGear(source=url, stream_mode=True, logging=True).start()

        numerator = 0
        while True:
            frame = stream.read()
            if frame is None:
                break

            print(f"Processing frame {numerator} from {video_name}")

            image_output_path = os.path.join(output_path_video, f"image_{numerator}.png")
            resized = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
            cv2.imwrite(image_output_path, resized)

            numerator += 1

        # Stop the stream
        stream.stop()
        print(f"Extracted {numerator} images from {video_name} to: {output_path_video}")

    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")

print("Image extraction from all URLs complete.")
