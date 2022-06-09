from rest_framework import serializers
from django.contrib.auth import get_user_model
from teams.models import Team

User = get_user_model()


class UserSeializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username',)


# 팀 페이지 조회 및 수정 및 팀장 등록 및 해제
# 전체/개별 팀 조회
class MyTeamSerializer(serializers.ModelSerializer):

    team_memeber = UserSeializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'
