from django.urls import path
from . import views


app_name = "calculator"
urlpatterns = [
    path('', views.optimize, name='optimize'),
    path('plants', views.choosePlants, name='choosePlants'),
    path('updateChoices/', views.updateChoices, name='updateChoices')
]
