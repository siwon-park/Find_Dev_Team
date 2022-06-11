from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.team), # 전체 팀 조회
    path('create/', views.team_create), # 팀 생성
    path('<int:team_pk>/', views.myteam), # 개별 팀 조회 및 수정
]
