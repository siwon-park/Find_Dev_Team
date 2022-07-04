<template>
  <div>
    <div v-if="{userInfo} !== null">
      {{this.userId}}
      {{this.profile}}
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

</style>