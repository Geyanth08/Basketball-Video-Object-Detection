from autodistill.detection import CaptionOntology
from autodistill_grounding_dino import GroundingDINO
import os

# Define ontology
ontology = CaptionOntology({
    "basketball player with blue shirt": "Maccabi player",
    "basketball player with white shirt": "Real Madrid player",
    "basketball orange ball": "ball",
    "person with black or orange shirt": "referee",
})


# Input folder containing combined images
input_folder = "/kaggle/input/basketball-frames"

# Output folder for annotations
output_folder = "/kaggle/working/dataset"
os.makedirs(output_folder, exist_ok=True)

# Thresholds
BOX_THRESHOLD = 0.3
TEXT_THRESHOLD = 0.3

# Initialize the Grounding DINO model
model = GroundingDINO(
    ontology=ontology,
    box_threshold=BOX_THRESHOLD,
    text_threshold=TEXT_THRESHOLD
)

# Annotate images
dataset = model.label(
    input_folder=input_folder,
    extension=".png",
    output_folder=output_folder
)

print("\nAnnotation completed.")