from paddleocr import PaddleOCR

# Initialize OCR with angle classifier enabled
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Use .predict() without 'cls' argument
result = ocr.predict('test4.jpg')

for page in result:     # <-- You need this loop!
    rec_texts = page.get('rec_texts', [])
    rec_scores = page.get('rec_scores', [])
    for text, score in zip(rec_texts, rec_scores):
        print(f"{text} (confidence: {score:.2f})")
