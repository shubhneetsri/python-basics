import cv2
import pytesseract

# Optional: Set tesseract executable path (required on Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def read_bad_text(image_path, show_images=True):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return ""

    # Resize (helps with small handwriting or low-res scans)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Show original image (optional)
    if show_images:
        cv2.imshow("Original", img)

    # 1. Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. Apply median blur to reduce noise
    blurred = cv2.medianBlur(gray, 3)

    # 3. Apply thresholding (Otsu's method)
    thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # 4. Optional: Dilate to thicken characters
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    dilated = cv2.dilate(thresh, kernel, iterations=1)

    # 5. Show preprocessed image (optional)
    if show_images:
        cv2.imshow("Preprocessed", dilated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 6. OCR configuration
    # --oem 3: Default OCR engine mode (LSTM + legacy)
    # --psm 6: Assume a single block of text (try other modes too if needed)
    custom_config = r'--oem 3 --psm 6'

    # 7. Run OCR
    extracted_text = pytesseract.image_to_string(dilated, config=custom_config)

    return extracted_text

# Example usage
image_file = "test5.jpg"
text_result = read_bad_text(image_file)
print("Extracted Text:")
print(text_result)
