# Define Main Function
if __name__ == '__main__':
    # Importing Python Modules:S1
    try:
        from pathlib import Path
    except Exception as error:
        print(f'ERROR - [Main:S1] - {str(error)}')

    # Define Folder And File Path:S2
    try:
        parent_folder_path = Path.cwd()
        images_folder_path = Path(parent_folder_path) / 'Images'
    except Exception as error:
        print(f'ERROR - [Main:S2] - {str(error)}')