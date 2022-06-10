import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    token: localStorage.getItem('token') || '',
    currentUser: {},
  },

  getters: {
    isLoggedIn: state => !!state.token,
    authHeader: state => ({Authorization: `Token ${state.token}`}),
    currentUser: state => state.currentUser
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, userData) => state.currentUser = userData

  },
  actions: {
    
    // 토큰 저장(로그인 시 토큰 저장)
    saveToken ({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    // 토큰 삭제(로그아웃 시 토큰 삭제)
    removeToken ({commit}) {
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    // 로그인
    login({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials,
      })
      .then(res => {
        const token = res.data.key
        dispatch('saveToken', token)
        dispatch('fetchCurrentUser')
        router.push({name: 'MainPage'})
      })
      .catch(err => {
        console.error(err.response.data)
        // 에러 정보를 저장해서 불러오기(?)
      })
    },

    // 회원가입
    signup({commit}, credentials) {
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials,
      })
      .then(res => {
        const token = res.data.key
        dispatch('saveToken', token)
        dispatch('fetchCurrentUser')
        router.push({ name: 'MainPage' })
      })
      .catch(err => {
        console.error(err.response.data)
        // 에러 정보를 저장해서 불러오기
      })
    },

    // 로그 아웃
    logout({getters, dispatch}) {
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        headers: getters.authHeader,
      })
      .then(() => {
        dispatch('removeToken')
        alert('성공적으로 로그아웃되었습니다.')
        localStorage.removeItem('vuex')
        router.push({name:"LoginView"})
      })
      .catch(err => {
        console.error(err.response.data)
      })
    },

    
    // 회원 탈퇴


    // 현재 유저(자기 자신) 정보 가져오기
    fetchCurrentUser({ commit, getters, dispatch }) {
      // 로그인 되어있을 경우에 정보를 가져옴
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.mypage(),
          method: 'get',
          headers: getters.authHeader,
        })
        .then(res => {
          commit('SET_CURRENT_USER', res.data)
        })
        .catch(err => {
          if( err.response.state === 401) {
            dispatch('removeToken')
            router.push({name: 'LoginView'})
          }
        })
      }
    },
  }
}