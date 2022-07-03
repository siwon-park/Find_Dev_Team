<template>
  <div>
    <div>
      <div class="container-fluid">
        <Flicking :options="{ circular: true }">
          <div class="d-flex justify-content-center">
            <TeamList v-for="(eachTeam, index) in teams" 
            :key="index"
            :eachTeam="eachTeam"
            class="mx-3">
            </TeamList>
          </div>
        </Flicking>
      </div>
      <br><br><br>
      <Flicking :options="{ circular: true }">
        <div class="d-flex justify-content-center">
          <MemberList 
          v-for="eachUser in allUsers" 
          :key="eachUser.id" 
          :eachUser="eachUser"
          class="mx-3"></MemberList>
        </div>
      </Flicking>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import {Flicking} from "@egjs/vue-flicking"
import TeamList from '@/components/MainPage/TeamList.vue'
import MemberList from '@/components/MainPage/MemberList.vue'

export default {
  name: 'MainPage',
  components: {
    TeamList,
    MemberList,
    Flicking,
  },
  methods: {
    ...mapActions(['fetchTeams', 'fetchAllUsers', 'fetchBookmarkings'])
  },
  computed: {
    ...mapGetters(['teams', 'allUsers', 'bookmarkings'])
  },
  created() {
    this.fetchTeams()
    this.fetchAllUsers()
  }

}
</script>

<style scoped>

</style>