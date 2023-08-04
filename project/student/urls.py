from django.urls import path
from .import views
urlpatterns = [
    path('', views.empform,name='insert'),
    path('<int:id>/',views.empform,name='updatedata'),
    path('list/',views.emplist,name='list'),
    path('delete/<int:id>',views.empdelete,name='deletedata')
]

