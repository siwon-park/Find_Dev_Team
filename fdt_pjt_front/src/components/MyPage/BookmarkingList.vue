<template>
  <div>
    나의 북마크 모아보기
    {{this.userId}}
    {{this.profile}}
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
    ...mapGetters(['profile',]),  
  },
  methods: {
    ...mapActions(['fetchProfile'])
    // 나의 북마크 모아보기에서 북마크 해제 기능을 구현할 것인가?
  },
  created() {
    // 매번 비동기 호출로 해결 안되면, allUser를 호출해서 userId가 일치하는 데이터를 넘기면 됨
    this.fetchProfile(this.userId)
  },
}
</script>

<style scoped>

</style>