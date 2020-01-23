from django.urls import path
from . import views

urlpatterns = [
    path('pojazdy', views.pojazd_list),
    path('pojazd/<int:pk>', views.pojazd_detail),
   # path('users/', views.UserList),
   # path('users/<int:pk>/', views.UserDetail),
    path('diagnosci', views.diagnosta_list),
    path('diagnosta/<int:pk>', views.diagnosta_detail),
    path('klienci', views.klient_list),
    path('klient/<int:pk>', views.klient_detail),
    path('badania', views.badanie_list),
    path('badanie/<int:pk>', views.badanie_detail),
]
