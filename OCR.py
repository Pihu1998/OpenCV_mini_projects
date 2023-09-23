from pytesseract import Output
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
filename = 'processed.jpg'
image = cv2.imread(filename)
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
image = cv2.resize(image, (1920, 1080))

# OCR on the image input
print("Result: ", pytesseract.image_to_string(image))

hImg,wImg,_ = image.shape
# boxes = pytesseract.image_to_boxes(image).

# Bounding box on recognised words
results = pytesseract.image_to_data(image)
for x,b in enumerate(results.splitlines()):
    if x!=0:
        b = b.split()
        print(b)
        if len(b)==12:

            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(image, (x,y), (w+x, h+y), (0,0,255), 3)
            cv2.putText(image, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)


cv2.imshow("Result",image)   
cv2.waitKey(0) 
