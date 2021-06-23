from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.createOrder,name='home'),
    path('update/',views.updateView,name='update'),
    path('delete/',views.deleteView,name='delete'),
]
