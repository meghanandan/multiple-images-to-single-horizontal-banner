from PIL import Image
import os

def merge_images(input_folder, output_path):
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))]

    if not image_files:
        print("No image files found in the folder.")
        return

    # Open the first image to get the size
    first_image_path = os.path.join(input_folder, image_files[0])
    base_image = Image.open(first_image_path)
    width, height = base_image.size

    # Create a new blank image with the total width and the height of the first image
    banner = Image.new('RGB', (len(image_files) * width, height))

    # Paste each image into the banner
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)
        banner.paste(image, (i * width, 0))

    # Save the merged banner
    banner.save(output_path)
    print(f"Merged images saved to {output_path}")

if __name__ == "__main__":
    input_folder = r'C:\Users\Administrator\Pictures\pics\banner'
    output_path = r'C:\Users\Administrator\Pictures\pics\banner\merged_banner.webp'

    merge_images(input_folder, output_path)
