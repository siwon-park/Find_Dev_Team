from rest_framework import serializers
from django.contrib.auth import get_user_model
from skills.models import Knowledge
from dj_rest_auth.registration.serializers import RegisterSerializer

from teams.models import Team
User = get_user_model()

# 로그인/회원가입/로그아웃/비밀번호 찾기/회원 탈퇴
class AccountSignUpSerializer(RegisterSerializer):
    sex = serializers.CharField(max_length=10)
    region = serializers.CharField(max_length=30) 
    position = serializers.CharField(max_length=30) 
    major = serializers.CharField(max_length=30)
    group = serializers.CharField(max_length=30)
    nickname = serializers.CharField(max_length=30)

    class Meta:
        model= User
        fields = ('sex', 'region', 'position', 'major', 'group', 'nickname',)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['sex'] = self.validated_data.get('sex', '')
        data['region'] = self.validated_data.get('region', '')
        data['position'] = self.validated_data.get('position', '')
        data['major'] = self.validated_data.get('major', '')
        data['group'] = self.validated_data.get('group', '')
        data['nickname'] = self.validated_data.get('nickname', '')

        return data


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
    my_team = serializers.CharField(max_length=50)

    def to_representation(self, instance):
        self.fields['my_team'] = TeamSerializer(read_only=True)
        return super(AccountSerializer, self).to_representation(instance)

    class Meta:
        model = User
        fields = ('id', 'username', 'sex', 'region', 'position', 'major', 'group', 'nickname', 'img', 'intro', 'kakao_chat', 'github_url', 'portfolio_url', 'strength', 'my_team',)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['sex'] = self.validated_data.get('sex', '')
        data['region'] = self.validated_data.get('region', '')
        data['position'] = self.validated_data.get('position', '')
        data['major'] = self.validated_data.get('major', '')
        data['group'] = self.validated_data.get('group', '')
        data['nickname'] = self.validated_data.get('nickname', '')
        data['img'] = self.validated_data.get('img', '')
        data['intro'] = self.validated_data.get('intro', '')
        data['kakao_chat'] = self.validated_data.get('kakao_chat', '')
        data['github_url'] = self.validated_data.get('github_url', '')
        data['portfolio_url'] = self.validated_data.get('portfolio_url', '')
        data['strength'] = self.validated_data.get('strength', '')
        data['my_team'] = self.validated_data.get('my_team', '')

        return data

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', )



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

