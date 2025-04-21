look at this code, i want to use the object detection, and the draw the b

from transformers import DetrFeatureExtractor
from transformers import TableTransformerForObjectDetection
import torch
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO
url = "https://github.com/shprintsin/OCR-examples/blob/main/input/klk_table.png?raw=true"
response = requests.get(url)
image = Image.open(BytesIO(response.content)).convert("RGB")
ratio=image.width/image.height
width=400
image.resize((int(ratio*width),width))

width, height = image.size
image.resize((int(width*0.5), int(height*0.5)))
feature_extractor = DetrFeatureExtractor()
encoding = feature_extractor(image, return_tensors="pt")
encoding.keys()
model = TableTransformerForObjectDetection.from_pretrained("microsoft/table-transformer-structure-recognition")
with torch.no_grad():
  outputs = model(**encoding)
  target_sizes = [image.size[::-1]]
results = feature_extractor.post_process_object_detection(outputs, threshold=0.6, target_sizes=target_sizes)[0]
# plot_results(image, results['scores'], results['labels'], results['boxes'])
# model.config.id2label


# x1,y1,x2,y2=detections[2]

# Convert results to detections
detections = sv.Detections.from_ultralytics(results)
image = cv2.imread(image_path)

# Define a custom color palette for each class
class_colors = [
    sv.Color(255, 0, 0),    # Red for "Caption"
    sv.Color(0, 255, 0),    # Green for "Footnote"
    sv.Color(0, 0, 255),    # Blue for "Formula"
    sv.Color(255, 255, 0),  # Yellow for "List-item"
    sv.Color(255, 0, 255),  # Magenta for "Page-footer"
    sv.Color(0, 255, 255),  # Cyan for "Page-header"
    sv.Color(128, 0, 128),  # Purple for "Picture"
    sv.Color(128, 128, 0),  # Olive for "Section-header"
    sv.Color(128, 128, 128),# Gray for "Table"
    sv.Color(0, 128, 128),  # Teal for "Text"
    sv.Color(128, 0, 0)     # Maroon for "Title"
]

# Initialize the BoxAnnotator with the custom color palette and increased thickness
box_annotator = sv.BoxAnnotator(
    color=sv.ColorPalette(class_colors),
    thickness=3  # Increased thickness for bounding boxes
)

# Annotate the image with bounding boxes
annotated_image = box_annotator.annotate(
    scene=image,
    detections=detections
)

# Initialize the LabelAnnotator with custom background and text colors
label_annotator = sv.LabelAnnotator(
    color=sv.ColorPalette(class_colors),  # Background colors matching bounding boxes
    text_color=sv.Color(255, 255, 255)    # White text for better readability
)

# Annotate the image with labels
annotated_image = label_annotator.annotate(
    scene=annotated_image,
    detections=detections
)

# Display the annotated image
sv.plot_image(annotated_image)
# plt.figure(figsize=(16,10))
# plt.imshow(image)
# ax = plt.gca()
# scores=results['scores']
# labels=results['labels']
# boxes=results['boxes']
