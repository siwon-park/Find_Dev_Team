<template>
  <div>
    <h1>팀 조회 페이지</h1>
    <p> {{ team.name }}</p>
    <p> {{ team.intro }}</p>
    <p> {{ team.leader }}</p>
    <div>
      <router-link :to="{ name: 'teamEdit', params: { teamId } }">
        <button>팀 수정 버튼</button>
      </router-link>

    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MyTeamPageView',
  data() {
    return{
      teamId: this.$route.params.teamId,
    }
  },
  computed:{
    ...mapGetters(['team']),
  },
  methods:{
    ...mapActions([
      'fetchTeam',
    ])
  },
  created(){
    this.fetchTeam(this.teamId)
  },
}
</script>

<style>

</style>