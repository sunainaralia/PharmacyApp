from django.urls import path
from .views import MedicineListCreateAPIView, MedicineRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('medicine/', MedicineListCreateAPIView.as_view(), name='medicine_list'),
    path('medicine/<int:pk>', MedicineRetrieveUpdateDestroyAPIView.as_view(),
         name='medicine'),
]
