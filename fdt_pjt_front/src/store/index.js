import Vue from 'vue'
import Vuex from 'vuex'
import accounts from './modules/accounts'
import teams from './modules/teams'
import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  modules: {
    accounts, teams,
  }
})
