import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from '@/views/MainPage/MainPage.vue'
import LoginForm from '@/views/Accounts/LoginForm.vue'
import MyTeamPageView from '@/views/Teams/MyTeamPageView.vue'
import TeamEditView from '@/views/Teams/TeamEditView.vue'
import TeamNewView from '@/views/Teams/TeamNewView.vue'

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

  // 개별 팀 조회
  {
    path: '/teams/:teamId',
    name: 'team',
    component: MyTeamPageView
  },

  // 팀 수정
  {
    path: '/teams/:teamId/edit',
    name: 'teamEdit',
    component: TeamEditView
  },

  // 팀 생성
  {
    path: '/new',
    name: 'teamNew',
    component: TeamNewView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
