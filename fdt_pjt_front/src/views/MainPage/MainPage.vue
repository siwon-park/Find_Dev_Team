<template>
  <div>
    <h1>메인페이지</h1>
    <div>
      <v-app>
      <TeamList v-for="(eachTeam, index) in teams" 
      :key="index"
      :eachTeam="eachTeam"></TeamList>
      </v-app>
      <hr>
      <hr>
      <MemberList v-for="eachUser in allUsers" :key="eachUser.id" :eachUser="eachUser"></MemberList>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import TeamList from '@/components/MainPage/TeamList.vue'
import MemberList from '@/components/MainPage/MemberList.vue'

export default {
  name: 'MainPage',
  components: {
    TeamList,
    MemberList,
  },
  methods: {
    ...mapActions(['fetchTeams', 'fetchAllUsers'])
  },
  computed: {
    ...mapGetters(['teams', 'allUsers'])
  },
  created() {
    this.fetchTeams()
    this.fetchAllUsers()
  }

}
</script>

<style>

</style>