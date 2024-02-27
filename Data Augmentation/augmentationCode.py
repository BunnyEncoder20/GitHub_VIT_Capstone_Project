from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import os
import shutil

# Define the paths for the input and output directories
input_dir = './Images'
output_dir = './Balanced'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Create the ImageDataGenerator with the desired transformations
datagen = ImageDataGenerator(
    rotation_range=40,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    vertical_flip=False,
    # width_shift_range=0.2,
    # height_shift_range=0.2,
    fill_mode='nearest'
)

# Loop through each folder in the input directory
for foldername in os.listdir(input_dir):
    # Create the corresponding folder in the output directory
    output_folder = os.path.join(output_dir, foldername)
    os.makedirs(output_folder, exist_ok=True)
    
    # Calculate the number of images in the input folder
    num_input_images = len(os.listdir(os.path.join(input_dir, foldername)))
    
    # Calculate the number of augmented images needed to reach approximately 2000 images for each image
    num_augmented_images_per_image = max(1, int((20 - num_input_images) / num_input_images)) + 1

    print(f"Processing folder: {foldername}\n InputFolder Images: {num_input_images}\n Augmentations Needed / Image: {num_augmented_images_per_image}\n",end='...\n')
    
    # Loop through each image in the current folder
    for filename in os.listdir(os.path.join(input_dir, foldername)):
        # Load the original image
        original_img_path = os.path.join(input_dir, foldername, filename)
        img = image.load_img(original_img_path, target_size=(256, 256))
        
        # Convert the image to a numpy array
        img_array = image.img_to_array(img)
        
        # Reshape the image array to match the expected input shape of the datagen
        input_batch = img_array.reshape(1, 256, 256, 3)
        
        # Copy the original image to the output folder
        shutil.copy(original_img_path, output_folder)
        
        # Generate augmented images and save them to the output folder
        i = 0
        for output in datagen.flow(input_batch, batch_size=1, save_to_dir=output_folder, save_prefix='aug', save_format='jpeg'):
            i += 1
            if i >= num_augmented_images_per_image:
                break
    print("Done✔️")
