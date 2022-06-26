<template>
  <div>
    <h1>프로필 수정</h1>
    <form @submit.prevent="updateRequest()">
      <div>
        <label for="nickname">Nickname:</label>
        <input v-model="currentUser.nickname" type="text" id="nickname" required />
      </div>
      <div>
        <label for="region">Region:</label>
        <input v-model="currentUser.region" type="text" id="region" required />
      </div>
      <div>
        <label for="sex">Sex:</label>
        <input v-model="currentUser.sex" type="text" id="sex" required />
      </div>
      <div>
        <label for="position">Position:</label>
        <input v-model="currentUser.position" type="text" id="position" required />
      </div>
      <div>
        <label for="major">major:</label>
        <input v-model="currentUser.major" type="text" id="major" required />
      </div>
      <div>
        <label for="group">group:</label>
        <input v-model="currentUser.group" type="text" id="group" required />
      </div>
      <div>
        <label for="img">img:</label>
        <input v-model="currentUser.img" type="text" id="img" required />
      </div>
      <div>
        <label for="intro">intro:</label>
        <input v-model="currentUser.intro" type="text" id="intro" required />
      </div>
      <div>
        <label for="kakao_chat">kakao_chat:</label>
        <input v-model="currentUser.kakao_chat" type="text" id="kakao_chat" required />
      </div>
      <div>
        <label for="github_url">github_url:</label>
        <input v-model="currentUser.github_url" type="text" id="github_url" required />
      </div>
      <div>
        <label for="portfolio_url">portfolio_url:</label>
        <input v-model="currentUser.portfolio_url" type="text" id="portfolio_url" required />
      </div>
      <div>
        <label for="strength">strength:</label>
        <input v-model="currentUser.strength" type="text" id="strength" required />
      </div>
      <div>
        <button>프로필 수정</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MyPageEdit',
  data() {
    return {

    }
  },
  computed: {
    ...mapGetters(['currentUser',])
  },
  methods: {
    ...mapActions(['fetchCurrentUser', 'updateProfile']),
    updateRequest() {
      const userData = {nickname: this.currentUser.nickname, region: this.currentUser.region, 
      sex: this.currentUser.sex, position:this.currentUser.position, major:this.currentUser.major,
      group: this.currentUser.group, img: this.currentUser.img, intro: this.currentUser.intro,
      kakao_chat: this.currentUser.kakao_chat, github_url: this.currentUser.github_url, 
      portfolio_url: this.currentUser.portfolio_url, strength: this.currentUser.strength,
      ...this.currentUser}
      this.updateProfile(userData)
    }
  },
  created() {
    this.fetchCurrentUser()
  },
}
</script>

<style>

</style>