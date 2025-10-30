import os
from PIL import Image

input_folder = "images_input"
output_folder = "images_output"

# Desired resize size (width, height)
new_size = (800, 600)

# ✅ Automatically create folders if they don’t exist
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Check if there are images to process
if not os.listdir(input_folder):
    print(f"⚠️ No images found in '{input_folder}' folder.")
    print("Please add some .jpg or .png images there and run again.")
    exit()

# Loop through each image in the folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize the image
        resized_img = img.resize(new_size)

        # Save resized image in output folder (same name)
        output_path = os.path.join(output_folder, filename)
        resized_img.save(output_path)

        print(f"✅ {filename} resized and saved to '{output_folder}'")

print("All images resized successfully!")
