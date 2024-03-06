from django.urls import path
from . import views


urlpatterns = [
    path('show/', views.predDisease, name="show"),
    path('upload_image/', views.upload_image, name="upload_image"),
    path('signup',views.signup,name='signup'),
]
