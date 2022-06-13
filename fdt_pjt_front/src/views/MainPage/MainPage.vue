<template>
  <div>
    <h1>메인페이지</h1>
    <div>
      <TeamList></TeamList>
      <hr>
      <hr>
      <MemberList></MemberList>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import TeamList from '@/components/MainPage/TeamList.vue'
import MemberList from '@/components/MainPage/MemberList.vue'

export default {
  name: 'MainPage',
  components: {
    TeamList,
    MemberList,
  },
  methods: {
    ...mapActions([])
  },

}
</script>

<style>

</style>