from ultralytics import YOLO

def main():
    # Load the YOLO model
    model = YOLO('yolov8s.yaml') # load the small model

    # Use the yaml file
    config_file_path = "/kaggle/working/dataset/data.yaml"
    project = "/kaggle/working/checkpoints"
    experiment = "small-Model"
    batch_size = 32 # reduce to 16 if you have memory errors

    # train the model
    results = model.train(data=config_file_path,
                          epochs=10,
                          project=project,
                          name=experiment,
                          batch=batch_size,
                          device=0,
                          patience=40,
                          imgsz=640,
                          val=True)

if __name__ == "__main__":
    main()