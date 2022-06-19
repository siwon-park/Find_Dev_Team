from ast import keyword
from unittest import result
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import *
from .serializers.team import *
from rest_framework import status

User = get_user_model()

# 전체 팀 조회
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly]) # 인증된 사용자는 모든 요청 가능, 인증되지 않은 사용자는 GET만 가능
def team(request):
    team_list = Team.objects.all()
    serializer = MyTeamSerializer(team_list, many=True) # QuerySet 형태로 데이터 삽입
    return Response(serializer.data)


# 팀 생성
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly]) # 인증된 사용자는 모든 요청 가능, 인증되지 않은 사용자는 GET만 가능
def team_create(request):
    serializer = CreateTeamSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        teamID = serializer.data.get('id')
        team = get_object_or_404(Team, pk=teamID)
        team.team_member.add(request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 개별 팀 조회 및 수정
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def myteam(request, team_pk):

    def myteam_get():
        team = get_object_or_404(Team, pk=team_pk)
        serializer = MyTeamSerializer(team)
        return Response(serializer.data)
    
    def myteam_put():
        team = get_object_or_404(Team, pk=team_pk)
        teamID = team.id
        if request.user.my_team_id == teamID:
            serializer = MyTeamSerializer(instance=team, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serializer = MyTeamSerializer(team)
                return Response(serializer.data)
    
    if request.method == 'GET':
        return myteam_get()
    elif request.method == 'PUT':
        return myteam_put()


# 팀원을 검색한 목록을 출력
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly]) # 인증된 사용자는 모든 요청 가능, 인증되지 않은 사용자는 GET만 가능
def member_search(request):
    member = request.GET.get('member', None) # request에서 query 값을 인식한다는 뜻
    
    if member: # 만약 사용자가 입력한 값이 있다면
        results = User.objects.filter(username__icontains=member)
    else: # 없으면 모든 객체값을 출력
        results = User.objects.all()

    serializer = UserSeializer(results, many=True)

    return Response(serializer.data)