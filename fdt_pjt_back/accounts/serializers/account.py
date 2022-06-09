from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from skills.models import Knowledge

User = get_user_model()

# 로그인/회원가입/로그아웃/비밀번호 찾기/회원 탈퇴

# account 필드 재정의
class AccountSerializer(serializers.ModelSerializer):
    
    sex = serializers.CharField(max_length=10)
    region = serializers.CharField(max_length=30) 
    position = serializers.CharField(max_length=30) 
    major = serializers.CharField(max_length=30)
    group = serializers.CharField(max_length=30)
    nickname = serializers.CharField(max_length=30)
    img = serializers.CharField(max_length=50)
    intro = serializers.CharField(max_length=200)
    kakao_chat = serializers.CharField(max_length=50)
    github_url = serializers.CharField(max_length=200)
    portfolio_url = serializers.CharField(max_length=200)
    strength = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('sex', 'region', 'position', 'major', 'group', 'nickname', 'img', 'intro', 'kakao_chat', 'github_url', 'portfolio_url', 'strength', )

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['sex'] = self.validated_data.get('profile_img', '')
        data['region'] = self.validated_data.get('school', '')
        data['position'] = self.validated_data.get('career', '')
        data['major'] = self.validated_data.get('introduce', '')
        data['group'] = self.validated_data.get('github_url', '')
        data['nickname'] = self.validated_data.get('blog_url', '')
        data['img'] = self.validated_data.get('notion_url', '')
        data['intro'] = self.validated_data.get('notion_url', '')
        data['kakao_chat'] = self.validated_data.get('notion_url', '')
        data['github_url'] = self.validated_data.get('notion_url', '')
        data['portfolio_url'] = self.validated_data.get('notion_url', '')
        data['strength'] = self.validated_data.get('notion_url', '')

        return data



class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge
        fields = '__all__'


# 마이페이지 조회 및 수정, 전체/개별 사용자 조회(팀이 없는 사용자들)
class MyPageSerializer(serializers.ModelSerializer):

    user_knowledge = KnowledgeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

# 북마크 조회, 등록 및 해제
class BookmarkSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'bookmarking',)

