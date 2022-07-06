from django.urls import path
from write_prescription.views import prescribeMedicineView
urlpatterns = [
    path('prescribeMedicine/', prescribeMedicineView.as_view(), name='prescribeMedicine'),

]