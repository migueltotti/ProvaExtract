from TextExtractor import extractText
from ImageExtractor import extractImages
from RemoveImages import removeUnnecessarilyImages


def main():
    path = "C:\\Users\\migue\\OneDrive\\Documentos\\2024_PV_impresso_D1_CD1.pdf"
    #extractText(filePath=path)
    extractImages(filePath=path)
    removeUnnecessarilyImages()

if __name__ == "__main__":
    main()