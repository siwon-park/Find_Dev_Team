from django.db import models
from django.conf import settings

class Team(models.Model):
    name = models.CharField(max_length=50) 
    intro = models.CharField(max_length=200) # 팀 소개
    theme = models.CharField(max_length=50, null=True, blank=True) # 팀 주제
    common_interest = models.CharField(max_length=200, null=True, blank=True) # 공통 흥미
    number = models.IntegerField(null=True, blank=True) # 현재 모집한 인원
    total_number = models.IntegerField(null=True, blank=True) # 총 모집할 인원
    kakao_chat = models.CharField(max_length=50, null=True, blank=True) # 팀 카카오 오픈 챗
    # 팀장
    reader = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reader_team')