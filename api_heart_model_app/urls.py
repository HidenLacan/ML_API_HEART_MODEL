from django.urls import path
from .views import Prediction_Heart

urlpatterns = [
    path('prediction/',Prediction_Heart.as_view(),name='predictionheart'),
    
    
]
