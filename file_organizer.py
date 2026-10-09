import os
import shutil

def organize_jpg_files(source_folder, destination_folder):
    # Check whether the source folder exists
    if not os.path.isdir(source_folder):
        print("Error: Source folder does not exist.")
        return

    # Create the destination folder if needed
    os.makedirs(destination_folder, exist_ok=True)

    moved_count = 0

    # Find and move JPG files
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            if os.path.isfile(source_path):
                if os.path.exists(destination_path):
                    print(f"Skipped {filename}: destination file already exists.")
                    continue

                shutil.move(source_path, destination_path)
                moved_count += 1
                print(f"Moved: {filename}")

    print(f"\nCompleted! Total JPG files moved: {moved_count}")


if __name__ == "__main__":
    source = input("Enter the source folder path: ").strip().strip('"')
    destination = input("Enter the destination folder path: ").strip().strip('"')

    organize_jpg_files(source, destination)