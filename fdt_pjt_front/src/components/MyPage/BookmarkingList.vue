<template>
  <div>
    <div v-if="{userInfo} !== null">
      <div class="back inner-content py-3 px-3 d-flex flex-column justify-content-evenly">
        <div>
          <div class="each-content d-f">
            닉네임: {{this.userInfo.nickname}}
          </div>
          <div class="each-content">
            포지션: {{this.userInfo.position}}
          </div>
          <div class="each-content">
            전공여부: {{this.userInfo.major}}
          </div>
          <div class="each-content">
            성별: {{this.userInfo.sex}}
          </div>
          <div class="each-content">
            지역: {{this.userInfo.region}}
          </div>
          <div class="each-content">
            <a :href="this.userInfo.kakao_chat"> 카카오 오픈챗</a>
          </div>
          <div class="each-content">
            <a :href="this.userInfo.github_url">GitHub</a>
          </div>
          <div class="each-content">
            소개 : {{this.userInfo.intro}}
          </div>
        </div>
      </div>
    </div>
  </div>

    
  
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name:'BookmarkingList',
  props: {
    userId: Number,
  },
  data() {
    return {
    }
  },
  computed: {
    ...mapGetters(['profile', 'allUsers',]),
    userInfo() {
      for (const user of this.allUsers) {
        if (user.id === this.userId) {
          return user
        }
      }
      return null
    }
  },
  methods: {
    ...mapActions(['fetchProfile'])
    // 나의 북마크 모아보기에서 북마크 해제 기능을 구현할 것인가?
  },
}
</script>

<style scoped>

.inner-content {
  height: 100%;
  background-color: #cde5eb;
  width: 300px;
  height: 300px;
  border-radius: 20px;
  font-weight: bolder;
  text-align: center;
  box-shadow: inset -2px -2px 6px 0 rgba(255, 255, 255, 0.2),
    inset 2px 2px 6px 0 rgba(97, 97, 97, 0.8);
  
}

.each-content {
  font-size: 16px;
}

.back{
  margin-right: 30px;
}
</style>