<template>
  <div>
    <form @submit.prevent="login(login_credentials)" action="POST">
      <div>
        유저이름:
        <label for="username"></label>
        <input type="text" v-model="login_credentials.username" placeholder="username" id="username">
      </div>
      <div>
        비밀번호:
        <label for="password"></label>
        <input type="password" v-model="login_credentials.password" placeholder="password" id="password">
      </div>
      <input type="submit">
    </form>
    <div>
      <router-link to="/signup"><button class="btn btn-primary">회원가입</button></router-link>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LoginForm',
  data() {
    return {
      login_credentials: {
        username: '',
        password: '',
      },
      // sign_credentials: {
      //   username: '',
      //   password1: '',
      //   password2: '',
      //   email:'',
      // },

    }
  },
  methods: {
    ...mapActions(['login',])
  }
}
</script>

<style>

</style>