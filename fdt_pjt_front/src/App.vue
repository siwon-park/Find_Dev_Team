<template>
  <div>
    <h1>안녕하세요?</h1>
    <router-link :to="{ name: 'teamNew' }">팀 생성 버튼</router-link><br>
    <!-- 로그인 로직이 아니라 팀 아이디가 있는지 없는지로 판단해야함 -->
    <!-- <router-link v-if="isLoggedIn" :to="{ name: 'team', params: { teamId: currentUser.my_team.id } }">내 팀 페이지</router-link><br> -->
    <router-link to='/login' v-if="!isLoggedIn">Login</router-link>
    <router-link @click.native="logout()" to='/login' v-if="isLoggedIn">Logout</router-link><br>
    <router-link :to="{ name: 'mypage' }">마이페이지</router-link><br>
    <router-view></router-view>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'App',

  data() {
    return {

    }
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser', ])
  },
  methods: {
    ...mapActions(['logout', 'fetchCurrentUser', ])
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
    /* background: linear-gradient(0deg, #B1D8F9, #D7CFF6, #FEEDD8); */
    /* background: radial-gradient(#B1D8F9, #D7CFF6, #FEEDD8); */
    background:
    linear-gradient(217deg, #B1D8F9, rgba(255,0,0,0) 70.71%),
    linear-gradient(127deg, #D7CFF6, rgba(0,255,0,0) 70.71%),
    linear-gradient(336deg, #FEEDD8, rgba(0,0,255,0) 70.71%);
    height: 100vh;

  }
</style>