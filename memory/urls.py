from . import views
from django.urls import path


urlpatterns = [
    path('', views.memory, name='memory'),
    path('save_leaderboard/', views.save_leaderboard, name='save_leaderboard')
]
