import streamlit as st
import cv2
from ultralytics import YOLO
from vidgear.gears import CamGear
import random
import time

# ------------------------------
# Cache colors for each class
# ------------------------------
class_colors = {}

def get_color(class_id):
    if class_id not in class_colors:
        class_colors[class_id] = tuple(random.randint(0, 255) for _ in range(3))
    return class_colors[class_id]

# ------------------------------
# Load YOLO model (CPU-friendly)
# ------------------------------
@st.cache_resource
def load_model(path):
    return YOLO(path)

# ------------------------------
# Detection function
# ------------------------------
def detect_objects(frame, model, threshold=0.3):
    results = model(frame, verbose=False)[0]
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        if score > threshold:
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
            color = get_color(int(class_id))
            label = results.names[int(class_id)].upper()
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return frame

# ------------------------------
# Main Streamlit App
# ------------------------------
def main():
    st.set_page_config(page_title="YOLO Video Detection", layout="wide")
    st.title("🎯 Real-Time YOLO Detection on YouTube Video")

    # Video URL input
    video_url = st.text_input("Enter YouTube video URL:", 
                              "https://youtu.be/C9XBFSOuamA?si=MVAQczEwnWWfgj8o")
    start_btn = st.button("▶ Start Detection")

    if start_btn:
        model_path = "D:\\M.Tech\\2nd Sem\\IVA_Lab\\Basketball_detection\\small-Model3\\weights\\best.pt"
        model = load_model(model_path)

        # Start stream
        stream = CamGear(source=video_url, stream_mode=True, logging=True).start()
        frame_display = st.image([])

        fps = 25
        delay = 1 / fps
        detect_every = 2  # Detect every N frames

        frame_count = 0
        last_time = time.time()

        if 'last_detected_frame' not in st.session_state:
            st.session_state.last_detected_frame = None

        stop_btn = st.button("🛑 Stop")

        while True:
            frame = stream.read()
            if frame is None or stop_btn:
                break

            frame = cv2.resize(frame, (640, 360))

            # Detection every N frames only
            if frame_count % detect_every == 0:
                detected_frame = detect_objects(frame.copy(), model)
                st.session_state.last_detected_frame = detected_frame
            else:
                detected_frame = st.session_state.last_detected_frame

            # Fallback in case detection is not available
            if detected_frame is None:
                detected_frame = frame

            frame_display.image(detected_frame, channels="BGR", use_container_width=True)

            elapsed = time.time() - last_time
            if elapsed < delay:
                time.sleep(delay - elapsed)
            last_time = time.time()
            frame_count += 1

        stream.stop()
        st.success("Detection stopped.")

if __name__ == "__main__":
    main()
