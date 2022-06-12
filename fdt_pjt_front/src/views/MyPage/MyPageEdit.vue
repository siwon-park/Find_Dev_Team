<template>
  <div>
    <h1>프로필 수정</h1>
    {{this.currentUser}}
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
    ...mapActions(['fetchCurrentUser',])
  },
  created() {
    this.fetchCurrentUser()
  },
}
</script>

<style>

</style>