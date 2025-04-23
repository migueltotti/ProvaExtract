import fitz  # PyMuPDF

def extractImages(filePath: str):
    doc = fitz.open(filePath)

    #page_index = 11

    #page = doc[page_index]
    #images = page.get_images(full=True)

    #for img_index, img in enumerate(images):
        #xref = img[0]
        #base_image = doc.extract_image(xref)
        #image_bytes = base_image["image"]
        #image_ext = base_image["ext"]
        #with open(f"page{page_index+1}_img{img_index+1}.{image_ext}", "wb") as f:
            #f.write(image_bytes)

    for page_index in range(len(doc)):
        page = doc[page_index]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            with open(f"page{page_index+1}_img{img_index+1}.{image_ext}", "wb") as f:
                f.write(image_bytes)