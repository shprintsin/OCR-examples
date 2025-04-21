INPUT="input/The census of the Jewish population in the South-Western region in 1765 - 1791 Issue 2.pdf"
from pymupdf import pymupdf
doc=pymupdf.open(input)
for i,page in enumerate(doc):
    for ind, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        with open(f"images/{i}_{ind}.{image_ext}", "wb") as f:
            f.write(image_bytes)
