import torch
from PIL import Image
from RealESRGAN import RealESRGAN
import os

# The `ImageUpscaler` class is a Python class that uses the RealESRGAN model to upscale images in a
# given directory. Not sure if this will be needed, it was just cool to try out.
class ImageUpscaler:

    def __init__(self, input_dir):
      self.input_dir = input_dir
      self.model = self.initialize_model()

    def initialize_model(self):
        """
        The function initializes a RealESRGAN model and loads pre-trained weights.
        :return: an instance of the RealESRGAN model that has been initialized and loaded with
        pre-trained weights.
        """
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = RealESRGAN(device)
        model.load_weights("weights/RealESRGAN_x4.pth", download=True)
        return model
    
    def upscale_images(self):
        """
        The function `upscale_images` takes an input directory, searches for image files, upscales them
        using a pre-trained model, and saves the upscaled images in a separate directory.
        """
        if os.path.exists(self.input_dir):
            for root, _, files in os.walk(self.input_dir):
                if "upscaled" in root:
                    continue
                output_dir = os.path.join(root, "upscaled")
                os.makedirs(output_dir, exist_ok=True)
                for file in files:
                    upscaled_file = os.path.join(output_dir, file)
                    if not os.path.exists(upscaled_file):
                        image = Image.open(os.path.join(root, file)).convert("RGB")
                        upscaled_image = self.model.predict(image)
                        upscaled_image.save(upscaled_file)
        else:
            raise FileNotFoundError("Error: Input directory does not exist. Please provide an existing directory.")