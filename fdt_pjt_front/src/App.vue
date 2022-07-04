<template>
  <div>
    <NavBar></NavBar>
    <!-- <router-link :to="{ name: 'teamcreate' }">팀 생성 버튼</router-link><br>
    <router-link v-if="currentUser.my_team !== null && isLoggedIn" :to="{ name: 'team', params: { teamId: currentUser.my_team.id } }">내 팀 페이지</router-link><br>
    <router-link to='/login' v-if="!isLoggedIn">Login</router-link>
    <router-link @click.native="logout()" to='/login' v-if="isLoggedIn">Logout</router-link><br>
    <router-link v-if="isLoggedIn" :to="{ name: 'mypage' }">마이페이지</router-link><br> -->
    <router-view></router-view>
    <FootBar></FootBar>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import NavBar from './NavBar.vue';
import FootBar from './FootBar.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    FootBar
  },
  data() {
    return {
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser',])
  },
  methods: {
    ...mapActions(['logout', 'fetchCurrentUser',])
  },
  created() {
    this.fetchCurrentUser()
  }
};
</script>

<style>
  * {
  font-family: 'Gowun Dodum', serif;
   }

  body {
    background:
    linear-gradient(217deg, #B1D8F9, rgba(255,0,0,0) 70.71%),
    linear-gradient(127deg, #D7CFF6, rgba(0,255,0,0) 70.71%),
    linear-gradient(336deg, #FEEDD8, rgba(0,0,255,0) 70.71%);
    height: 100vh;

  }
</style>