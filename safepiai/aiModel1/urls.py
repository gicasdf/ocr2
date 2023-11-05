from django.urls import path
from .views import process_images
from .views import OCRThreeResultView

urlpatterns = [
    #path('admin/process_photos/', views.process_photos, name='process_photos'),
    path('process_images/', process_images, name='process_images'),
    path('ocr_three_result/', OCRThreeResultView.as_view(), name='ocr_three_result'),
]
