from django.urls import path
from Shop import views
from .views import Kid, Crdio, kidsDetail, Gym_equipment, Cloth, gym_equipmentDetail, cardioDetail, clothesDetail

urlpatterns = [
    path('kids/', Kid.as_view(), name='kid'),
    path('about/', views.about),
    path('kidsdetail/<str:name>/', kidsDetail.as_view(), name='kidsdetail'),
    path('gym_euipmentsdetail/<str:name>/', gym_equipmentDetail.as_view(), name='gymeuipmentdetail'),
    path('cardiodetail/<str:name>/', cardioDetail.as_view(), name='cardiodetail'),
    path('clothesdetail/<str:name>/', clothesDetail.as_view(), name='clothesdetail'),
    path('cardio/', Crdio.as_view(), name='cardio'),
    path('clothes/', Cloth.as_view(), name='clothes'),
    path('gym_equipments/', Gym_equipment.as_view(), name='gym_equipment'),
]
