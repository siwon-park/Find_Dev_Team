from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.team_list), # 전체 팀 조회
    path('<int:team_pk>/', views.team_pick), # 개별 팀 조회
    path('<int:team_pk>/teampage/', views.myteam), # 팀 페이지 조회 및 수정 및 팀장 등록 및 해제
]
