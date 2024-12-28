from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_score, name='search_score'),
    path('dash-board', views.dashboard, name='dash_board'),
    path('top-student', views.top_student, name='top_student')
]