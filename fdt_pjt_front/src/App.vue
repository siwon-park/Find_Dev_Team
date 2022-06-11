<template>
  <div>
    <h1>안녕하세요?</h1>
    <router-link to='/login' v-if="!isLoggedIn">Login</router-link>
    <router-link @click.native="logout()" to='/login' v-if="isLoggedIn">Logout</router-link>
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
    ...mapGetters(['isLoggedIn',])
  },
  methods: {
    ...mapActions(['logout',])
  }
};
</script>

<style>

</style>