import pytesseract
from PIL import Image
import os

def perform_ocr(image_path):
    """
    Perform OCR on the given image and return the extracted text.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        str: Extracted text from the image
    """
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Perform OCR
        text = pytesseract.image_to_string(img)
        
        return text
    except Exception as e:
        print(f"Error performing OCR: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    input_dir = "input"
    if os.path.exists(input_dir):
        for filename in os.listdir(input_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(input_dir, filename)
                print(f"\nProcessing {filename}:")
                result = perform_ocr(image_path)
                if result:
                    print("Extracted text:")
                    print(result)
                else:
                    print("No text could be extracted.")
    else:
        print(f"Input directory '{input_dir}' not found.") 