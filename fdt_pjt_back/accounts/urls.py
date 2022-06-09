from django.urls import path
from . import views

# # 회원가입(POST) : account/signup/
# # 프로필 정보 조회 및 수정(GET/PUT) : account/user
# # 비밀번호 번형(POST) : account/password/change/
# # 비밀번호 찾기(POST) : account/password/reset/
app_name = 'accounts'

urlpatterns = [
    # path('signout/', views.signout), # 회원탈퇴
    path('', views.user_list), # 전체 사용자 조회(팀이 없는 사용자)
    path('<int:user_pk>/', views.user_pick), # 개별 사용자 조회
    path('<int:user_pk>/mypage/', views.mypage), # 마이페이지 조회 및 수정
    path('<int:user_pk>/bookmark/', views.bookmark), # 북마크 조회 및 등록 및 해제
    
]
