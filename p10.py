import img2pdf
from PIL import Image
import os

img_path = 'D:1.png'

pdf_path = 'D:1.pdf'

image = Image.open(img_path)

pdf_bytes = img2pdf.convert(image.filename)

file = open(pdf_path, "wb")

file.write(pdf_bytes)

image.close()

file.close()

print("SUCCESSFULLY MADE PDF FILE.")
print("this program is prepared by om and id :d21ce176")  