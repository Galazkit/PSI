from django.urls import path
from . import views

urlpatterns = [
    path('pojazdy', views.pojazd_list.as_view()),
    path('pojazd/<int:pk>', views.pojazd_detail.as_view()),
    #path('users/', views.UserList.as_view()),
    #path('users/<int:pk>/', views.UserDetail.as_view()),
    path('diagnosci', views.diagnosta_list),
    path('diagnosta/<int:pk>', views.diagnosta_detail),
    path('klienci', views.klient_list),
    path('klient/<int:pk>', views.klient_detail),
    path('badania', views.badanie_list),
    path('badanie/<int:pk>', views.badanie_detail),
]