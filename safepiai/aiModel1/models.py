from django.db import models

from django.db import models

class OCRModel(models.Model):
    name = models.CharField(max_length=100)
    # Add fields for your AI model as needed

    def __init__(self, model_path):
        #모델 초기화 코드
        pass
    def process_image(self, image_path):
        pass


class UploadedImage:
    pass