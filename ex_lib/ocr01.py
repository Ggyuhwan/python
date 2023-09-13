# pip install easyOCR
# pip install opencv-python
import easyocr
reader = easyocr.Reader(['ko'])
results = reader.readtext('img/image4.jpeg')
for result in results:
    text = result[1]
    print(text)