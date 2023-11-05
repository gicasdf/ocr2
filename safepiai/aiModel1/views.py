from django.shortcuts import render
from PIL import Image
from .models import UploadedImage

# Define a function to process an image with your AI model
def process_image(input_image_path, output_image_path):
    images = UploadedImage.objects.all()

    for image in images:
        input_image_path = image.image.path

        # Load the image
        input_image = Image.open(input_image_path)

        # Process the image with your OCR model
        processed_text = process_image_with_ocr(input_image)

        # Save the OCR result to the database
        image.processed_text = processed_text
        image.save()
