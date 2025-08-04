import easyocr
import cv2
import numpy as np

# Load the image using OpenCV
image_path = 'test.jpg'
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Could not load image {image_path}")
    exit()

# Resize image to improve OCR accuracy
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Preprocess the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)
thresh = cv2.adaptiveThreshold(
    blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 15
)
processed_img = cv2.bitwise_not(thresh)

# Save preprocessed image (optional)
cv2.imwrite('processed_test2.png', processed_img)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Run OCR on the preprocessed image
result = reader.readtext('processed_test2.png')

# Initialize a variable to hold full extracted text
full_text = []

# Process each detection
for bbox, text, conf in result:
    print(f"{text} (confidence: {conf:.2f})")
    if conf >= 0.5:
        full_text.append(text)

        # Draw bounding box
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))
        cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

        # Put text label
        cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

# Save output image with annotations
cv2.imwrite('output_with_text_boxes.png', img)

# Print all extracted text
print("\n📝 Full Extracted Text:")
print("\n".join(full_text) if full_text else "No high-confidence text found.")
