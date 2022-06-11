from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import *
from .serializers.account import *
from rest_framework import status

User = get_user_model()

# 회원탈퇴
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def signout(request):
    request.user.delete()
    data = {
        'content': '정상적으로 회원탈퇴 처리되었습니다.',
    }
    return Response(data, status=status.HTTP_204_NO_CONTENT)


# 전체 사용자 조회(팀이 없는 사용자)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly]) # 인증된 사용자는 모든 요청 가능, 인증되지 않은 사용자는 GET만 가능
def user_list(request):
    user_list = User.objects.filter(my_team__isnull=True)
    serializer = MyPageSerializer(user_list, many=True)
    return Response(serializer.data)

# 개별 사용자 조회(팀이 없는 사용자)
# 애초에 목록에 팀이 없는 사용자만 오픈됨
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly]) # 인증된 사용자는 모든 요청 가능, 인증되지 않은 사용자는 GET만 가능
def user_pick(request, user_pk):
    user_list = User.objects.filter(my_team__isnull=True)
    user_pick = get_object_or_404(user_list, pk=user_pk)
    serializer = MyPageSerializer(user_pick)
    return Response(serializer.data)

# 마이페이지 조회 및 수정
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def mypage(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    def mypage_get():
        serializer = MyPageSerializer(user)
        return Response(serializer.data)
    
    def mypage_put():
        if request.user == user:
            serializer = MyPageSerializer(instance=user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serializer = MyPageSerializer(user)
                return Response(serializer.data)
    
    if request.method == 'GET':
        return mypage_get()
    elif request.method == 'PUT':
        return mypage_put()

# 북마크 조회, 등록 및 해제
@api_view(['GET' ,'POST'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def bookmark(request, user_pk):

    def bookmark_get():
        # 나의 북마크 조회
        user = get_object_or_404(User, pk=user_pk)
        serializer = BookmarkSerializers(user)
        return Response(serializer.data)

    def bookmark_post():
        # user_pk : 북마크를 하려는 사용자의 pk
        bookmarked_user = get_object_or_404(User, pk=user_pk)
        user = request.user

        # 본인 확인
        if bookmarked_user != user:
            if user.bookmarking.filter(pk=bookmarked_user.pk).exists():
                user.bookmarking.remove(bookmarked_user)
            else:
                user.bookmarking.add(bookmarked_user)

            serializer = BookmarkSerializers(user)
            return Response(serializer.data)
        else:
            data = {
                'content': f'본인을 북마크 할 수 없습니다.'
            }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    
    if request.method == 'GET':
        return bookmark_get()
    elif request.method == 'POST':
        return bookmark_post()
