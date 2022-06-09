from django.db import models
from django.conf import settings

class Skill(models.Model):
    name = models.CharField(max_length=50)
    # User와의 중개 테이블 작성
    user_skill = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Knowledge')


class Knowledge(models.Model):
    level_choices = [
        ("5", "⭐⭐⭐⭐⭐"),
        ("4", "⭐⭐⭐⭐"),
        ("3", "⭐⭐⭐"),
        ("2", "⭐⭐"),
        ("1", "⭐"),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_knowledge')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skill_knowledge')
    level = models.CharField(
        choices=level_choices,
        max_length=30
    ) 
