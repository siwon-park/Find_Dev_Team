<template>
  <div>
    <h1>팀 수정 폼 페이지</h1>
    <p>{{ currentUser }}</p>
    <form @submit.prevent="onSubmit()" action="POST">
      <div>
        팀 명:
        <label for="name"></label>
        <input type="text" v-model="newTeam.name" placeholder="name" id="name">
      </div>
      <div>
        팀 소개:
        <label for="intro"></label>
        <input type="text" v-model="newTeam.intro" placeholder="intro" id="intro">
      </div>
      <input type="submit">
    </form>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
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
        team_member: this.team.team_member,
      }

    }
  },

  computed: {
    ...mapGetters(['currentUser',])
  },


  methods: {
    ...mapActions(['createTeam', 'updateTeam', 'fetchCurrentUser',]),
    onSubmit(){
      if(this.action === 'create') {
        this.newTeam.leader = this.currentUser.id
        this.newTeam.team_member = [
          { id: this.currentUser.id,
          username: this.currentUser.username}
        ]
        this.createTeam({team: this.newTeam, userInfo: this.currentUser})
        alert("등록되었습니다.")
      }
      else if (this.action === 'update'){
        const payload = {
          id: this.team.id,
          leader: this.currentUser.id,
          ...this.newTeam,
        }
        this.updateTeam(payload)
        alert("수정되었습니다.")
      }
    }
  },
  created() {
    this.fetchCurrentUser()
  }

}
</script>

<style>

</style>