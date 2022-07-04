from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete_item/<str:pk>', views.delete_item, name="delete_item"),
    path('cross_off/<str:pk>', views.cross_off, name="cross_off"),
    path('uncross/<str:pk>', views.uncross, name="uncross"),
    path('edit/<str:pk>', views.edit, name="edit"),

]