import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from '@/views/MainPage/MainPage.vue'
import LoginForm from '@/views/Accounts/LoginForm.vue'
import MyTeamPageView from '@/views/Teams/MyTeamPageView.vue'
import SignUpModal from '@/views/Accounts/SignUpModal.vue'
import MyPage from '@/views/MyPage/MyPage.vue'
import MyPageEdit from '@/views/MyPage/MyPageEdit.vue'
import MyBookmarks from '@/views/MyPage/MyBookmarks.vue'
import TeamCreateForm from '@/components/Teams/TeamCreateForm'

Vue.use(VueRouter)

const routes = [
  { // 메인 페이지
    path: '/',
    name: 'main',
    component: MainPage
  },
  { // 로그인 페이지
    path: '/login',
    name: 'login',
    component: LoginForm
  },
  { // 회원가입 페이지
    path: '/signup',
    name: 'signup',
    component: SignUpModal
  },
  { // 마이페이지
    path: '/mypage',
    name: 'mypage',
    component: MyPage
  },
  { // 마이페이지 수정
    path: '/mypage/edit',
    name: 'mypageedit',
    component: MyPageEdit
  },
  { // 개별 팀 조회
    path: '/teams/:teamId',
    name: 'team',
    component: MyTeamPageView
  },
  { // 북마크 모아보기
    path: '/mypage/bookmarkings',
    name: 'mybookmarkings',
    component: MyBookmarks,
  },
  { // 팀 생성
    path: '/team/new',
    name: 'teamcreate',
    component: TeamCreateForm,
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
