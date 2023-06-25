import torch
from PIL import Image
from RealESRGAN import RealESRGAN
import os

class ImageUpscaler:

    def __init__(self, input_dir):
      self.input_dir = input_dir
      self.model = self.initialize_model()

    def initialize_model(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model = RealESRGAN(device)
        model.load_weights("weights/RealESRGAN_x4.pth", download=True)
        return model
    
    def upscale_images(self):
        if os.path.exists(self.input_dir):
            for root, _, files in os.walk(self.input_dir):
                if "upscaled" in root:
                    continue
                output_dir = os.path.join(root, "upscaled")
                os.makedirs(output_dir, exist_ok=True)
                for file in files:
                    image = Image.open(os.path.join(root, file)).convert("RGB")
                    upscaled_image = self.model.predict(image)
                    upscaled_image.save(os.path.join(output_dir, file))
        else:
            raise FileNotFoundError("Error: Input directory does not exist. Please provide an existing directory.")