from django.urls import path
from news1.views import News1List
urlpatterns = [
    path('', News1List.as_view(), name='list'),
]
