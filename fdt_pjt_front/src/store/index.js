import Vue from 'vue'
import Vuex from 'vuex'
import accounts from './modules/accounts'
import teams from './modules/teams'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    accounts, teams,
  }
})
