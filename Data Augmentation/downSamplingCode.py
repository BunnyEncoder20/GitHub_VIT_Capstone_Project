import random
import os
import shutil

# Define the paths for the input and output directories
input_dir = './Images'
output_dir = './Balanced'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through each folder in the input directory
for foldername in os.listdir(input_dir):
    # Create the corresponding folder in the output directory
    output_folder = os.path.join(output_dir, foldername)
    os.makedirs(output_folder, exist_ok=True)
    print(f"Processing folder: {foldername}",end='...')
    
    # Get the list of image filenames in the current class directory
    image_filenames = os.listdir(os.path.join(input_dir, foldername))
    
    # Randomly select 2700 images
    selected_images = random.sample(image_filenames, 10)
    
    # Move the selected images to the output folder
    for filename in selected_images:
        # Get the path to the current image
        image_path = os.path.join(input_dir, foldername, filename)
        
        # Move the image to the output folder
        new_image_path = os.path.join(output_folder, filename)
        shutil.move(image_path, new_image_path)
    print("Done✔️")

















