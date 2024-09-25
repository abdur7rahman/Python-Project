from PIL import Image
import numpy as np

# Load the images
foreground = Image.open('img1.jpg')  # Image with green screen
background = Image.open('img2.jpg')      # New background image

# Resize background to match foreground
background = background.resize(foreground.size)

# Convert images to numpy arrays
foreground_np = np.array(foreground)
background_np = np.array(background)

# Define a threshold for green (you can tweak these values)
lower_green = np.array([0, 150, 0])  # Lower threshold for green
upper_green = np.array([120, 255, 120])  # Upper threshold for green

# Create a mask where green pixels are detected
mask = np.all((foreground_np >= lower_green) & (foreground_np <= upper_green), axis=-1)

# Replace green screen with the background
foreground_np[mask] = background_np[mask]

# Convert the result back to a PIL image
final_image = Image.fromarray(foreground_np)

# Save or show the result
final_image.save('output_image.jpg')
final_image.show()
