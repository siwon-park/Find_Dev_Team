<template>
  <div>
    <h1>팀 조회 페이지</h1>
    <p> 팀 명 : {{ team.name }}</p>
    <p> 팀 소개 : {{ team.intro }}</p>
    <p> 리더 : {{ team.leader }}</p>
    <p> 주제 : {{ team.theme }}</p>
    <p> 흥미 : {{ team.common_interest }}</p>
    <p> 현재 인원 수 : {{ team.team_member.length }}</p>
    <p> 모집 인원 : {{ team.total_number }}</p>
    <p> 카카오 오픈챗 : {{ team.kakao_chat }}</p>
    <p> 팀 멤버 : {{ team.team_member }}</p>
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