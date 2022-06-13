import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    token: localStorage.getItem('token') || '',
    currentUser: {},
    authError: null,
    profile: {},
    allUsers:{},
  },

  getters: {
    isLoggedIn: state => !!state.token,
    authHeader: state => ({Authorization: `Token ${state.token}`}),
    currentUser: state => state.currentUser,
    authError: state => state.authError,
    profile: state => state.profile,
    allUsers: state => state.allUsers,
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, userData) => state.currentUser = userData,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_ALL_USERS: (state, allUsersData) => state.allUsers = allUsersData,
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
        router.push({ name: 'main'})
      })
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },

    // 회원가입
    signup({commit, dispatch}, credentials) {
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials,
      })
      .then(res => {
        const token = res.data.key
        dispatch('saveToken', token)
        dispatch('fetchCurrentUser')
        router.push({ name: 'main' })
      })
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },

    // 로그 아웃
    logout({ commit, getters, dispatch }) {
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        headers: getters.authHeader,
      })
      .then(() => {
        dispatch('removeToken')
        alert('성공적으로 로그아웃되었습니다.')
        localStorage.removeItem('vuex')
        router.push({name:"login"})
      })
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },

    // 회원 탈퇴(만들어야함)
    signout({getters}) {
      if (confirm('정말 탈퇴하시겠습니까?')) {
        axios({
          url: drf.accounts.signout(),
          method: 'post',
          headers: getters.authHeader,
        })
        .then(() => {
          localStorage.removeItem('vuex')
          alert('성공적으로 회원탈퇴 처리')
          router.push({name: 'login'})
        })
        .catch(err => {
          console.error(err.response.data)
        })
      }
    },

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
          if (err.response.state === 401) {
            dispatch('removeToken')
            router.push({name: 'login'})
          } else if (err.response.state === 404) {
            router.push({name: 'NotFound404'})
          }
        })
      } else {
        alert('로그인이 필요한 서비스입니다.')
        router.push({name: 'login'})
      }
    },

    // 프로필 수정
    updateProfile({ commit, getters }, userData) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.mypage(),
          method: 'put',
          data: userData,
          headers: getters.authHeader,
        })
        .then(res => {
          commit('SET_CURRENT_USER', res.data)
          router.push({ name: 'mypage' })
        })
        .catch(err => {
          console.error(err.response.data)
        })
      }
    },

    // 다른 유저 프로필 조회
    fetchProfile({commit, getters}, userId) {
      axios({
        url: drf.accounts.profile(userId),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_PROFILE', res.data)
      })
      .catch(err => {
        if (err.response.state === 404) {
          router.push({name: 'NotFound404'})
        }
      })
    },

    // 전체 유저 조회
    fetchAllUsers({ commit }) {
      axios({
        url: drf.accounts.userlist(),
        method: 'get',
      })
      .then(res => {
        commit('SET_ALL_USERS', res.data)
      })
      .catch(err => {
        console.error(err.response.data)
      })
    },

  }
}