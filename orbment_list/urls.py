from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orbments/', views.OrbmentListView.as_view(), name='orbments'),
    path('orbment/<int:pk>', views.OrbmentDetailView.as_view(), name='orbment-detail'),
]

