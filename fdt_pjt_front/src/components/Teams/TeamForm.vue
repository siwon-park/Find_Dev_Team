<template>
  <div>
    <h1>팀 수정 폼 페이지</h1>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'TeamForm',
  props:{
    team: Object,
    action: String,
  },
  data(){
    return {
      newTeam:{
        name: this.team.name,
        intro: this.team.intro,
        leader: this.team.leader,
      }

    }
  },

  methods: {
    ...mapActions(['createTeam', 'updateTeam']),
    onSubmit(){
      if(this.action === 'create') {
        this.createTeam(this.newTeam)
        alert("등록되었습니다.")
      }
      else if (this.action === 'update'){
        const payload = {
          id: this.team.id,
          ...this.newTeam,
        }
        this.updateTeam(payload)
        alert("수정되었습니다.")
      }
    }
  }

}
</script>

<style>

</style>