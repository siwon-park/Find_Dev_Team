<template>
  <div>
    <form @submit.prevent="signup(signup_credentials)">
      <div>
        <label for="username">Username: </label>
        <input v-model="signup_credentials.username" type="text" id="username" required/>
      </div>
      <div>
        <label for="password1">Password: </label>
        <input v-model="signup_credentials.password1" type="password" id="password1" required />
      </div>
      <div>
        <label for="password2">Password Confirmation:</label>
        <input v-model="signup_credentials.password2" type="password" id="password2" required />
      </div>
      <div>
        <label for="nickname">Nickname:</label>
        <input v-model="signup_credentials.nickname" type="text" id="nickname" required />
      </div>
      <div>
        <label for="region">Region:</label>
        <input v-model="signup_credentials.region" type="text" id="region" required />
      </div>
      <div>
        <label for="sex">Sex:</label>
        <input v-model="signup_credentials.sex" type="text" id="sex" required />
      </div>
      <div>
        <label for="position">Position:</label>
        <input v-model="signup_credentials.position" type="text" id="position" required />
      </div>
      <div>
        <label for="major">major:</label>
        <input v-model="signup_credentials.major" type="text" id="major" required />
      </div>
      <div>
        <label for="group">group:</label>
        <input v-model="signup_credentials.group" type="text" id="group" required />
      </div>
      <div>
        <button>Signup</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'SignUpForm',
  data() {
    return {
      signup_credentials: {
        username: '',
        password1: '',
        password2: '',
        sex: '',
        region: '',
        position: '',
        major: '',
        group: '', // 지역 반
        nickname: '',
      }
    }
  },
  methods: {
    ...mapActions(['signup',])
  }
}
</script>

<style>

</style>