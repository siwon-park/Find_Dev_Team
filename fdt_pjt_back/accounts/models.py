from tokenize import group
from django.db import models
from django.contrib.auth.models import AbstractUser

from teams.models import Team

class User(AbstractUser):
    # 성별 항목
    sex_choices = [
        ("male", "남"),
        ("female", "여"),
    ]

    # 지역 항목
    region_choices = [
        ("seoul", "서울"),
        ("daejeon", "대전"),
        ("kwang", "광주"),
        ("bu", "부울경"),
        ("gu", "구미"),
    ]
    # 역할 항목
    position_choices = [
        ("back", "백엔드"),
        ("front", "프론트엔드"),
    ]

    # 전공 여부
    major_choices = [
        ("yes", "전공"),
        ("no", "비전공"),
    ]
    # 성별
    sex = models.CharField(
        choices=sex_choices,
        max_length=10
    )
    # 지역
    region = models.CharField(
        choices=region_choices,
        max_length=30
    )

    # 희망 포지션
    position = models.CharField(
        choices=position_choices,
        max_length=30
    ) 

    # 전공 여부
    major = models.CharField(
        choices=major_choices,
        max_length=30
    ) 

    group = models.CharField(max_length=30) # 반
    nickname = models.CharField(max_length=30)
    img = models.CharField(max_length=50, null=True, blank=True)
    intro = models.CharField(max_length=200, null=True, blank=True)
    kakao_chat = models.CharField(max_length=50)
    github_url = models.CharField(max_length=200, null=True, blank=True)
    portfolio_url = models.CharField(max_length=200, null=True, blank=True)
    strength = models.CharField(max_length=50, null=True, blank=True) # 강점

    # 팀
    my_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_memeber', null=True, blank=True)
    # 북마킹
    bookmarking = models.ManyToManyField('self', symmetrical=False, related_name='bookmarked_users', blank=True)
