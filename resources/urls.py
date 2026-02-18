from django.urls import path

from resources import views
from resources.views import ResourceDetailView

urlpatterns = [
    path('', views.resource_list, name='catalogue'),
    path('resource/<int:pk>/', ResourceDetailView.as_view(), name='resource_detail'),
]