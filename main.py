# Define Main Function
if __name__ == '__main__':
    # Importing Python Modules:S1
    try:
        from pathlib import Path
        import cv2
        import pytesseract
    except Exception as error:
        print(f'ERROR - [Main:S1] - {str(error)}')

    # Define Folder And File Path:S2
    try:
        parent_folder_path = Path.cwd()
        images_folder_path = Path(parent_folder_path) / 'Images'
    except Exception as error:
        print(f'ERROR - [Main:S2] - {str(error)}')

    # Discover Image Files:S3
    try:
        image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
        image_files = [
            file_path
            for file_path in images_folder_path.iterdir()
            if file_path.is_file() and file_path.suffix.lower() in image_extensions
        ]
        if not image_files:
            raise FileNotFoundError(f'No image files found in {images_folder_path}')
        target_image_path = image_files[0]
    except Exception as error:
        print(f'ERROR - [Main:S3] - {str(error)}')

    # Load Image:S4
    try:
        loaded_image = cv2.imread(str(target_image_path))
        if loaded_image is None:
            raise ValueError(f'Unable to load image from {target_image_path}')
    except Exception as error:
        print(f'ERROR - [Main:S4] - {str(error)}')

    # Convert To Grayscale:S5
    try:
        grayscale_image = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2GRAY)
    except Exception as error:
        print(f'ERROR - [Main:S5] - {str(error)}')

    # Apply Binary Threshold:S6
    try:
        _, black_white_image = cv2.threshold(grayscale_image, 150, 255, cv2.THRESH_BINARY)
    except Exception as error:
        print(f'ERROR - [Main:S6] - {str(error)}')

    # Run OCR:S7
    try:
        extracted_text = pytesseract.image_to_string(black_white_image)
    except Exception as error:
        print(f'ERROR - [Main:S7] - {str(error)}')

    # Print OCR Text:S8
    try:
        print('--- OCR TEXT START ---')
        print(extracted_text)
        print('--- OCR TEXT END ---')
    except Exception as error:
        print(f'ERROR - [Main:S8] - {str(error)}')
