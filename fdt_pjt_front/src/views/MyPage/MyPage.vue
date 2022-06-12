<template>
  <div>
    <h1>나의 프로필 페이지</h1>
    {{this.currentUser}}
  </div>
    
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MyPage',
  computed: {
    ...mapGetters(['currentUser',])
  },
  methods: {
    ...mapActions(['fetchCurrentUser',])

  },
  created() {
    this.fetchCurrentUser()
  }
}
</script>

<style>

</style>