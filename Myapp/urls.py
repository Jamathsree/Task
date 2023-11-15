from django.urls import path
from .views import register_user, login_user, ExamList

urlpatterns = [
    path('register_user/', register_user, name='register_user'),
    path('login_user/', login_user, name='login_user'),
    path('ExamList/', ExamList.as_view(), name='ExamList'),
    # Add URL for exam detail view or submission endpoint if needed
]

