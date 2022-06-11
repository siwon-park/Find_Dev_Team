import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from '@/views/MainPage/MainPage.vue'
import LoginForm from '@/views/Accounts/LoginForm.vue'

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

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
