from django.urls import path,include
from . import views

app_name = 'test_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register, name='register'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('play', views.play, name='play'),
    path('submission-result/<int:attempted_question_pk>', views.submission_result, name='submission_result'),
    path('user-home', views.user_home, name='user_home'),
    path('login', views.login_view, name='login'),
    path('logout',views.logout_view, name='logout'),

]


