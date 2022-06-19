<template>
  <v-app>
    <h4>팀 수정 폼</h4>
    <p>{{ currentUser }}</p>
    <p>{{ allUsers}}</p>
    <form @submit.prevent="onSubmit">
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
      <!-- 팀 멤버 등록 -->
      팀 멤버:
        <label for="team_member"></label>
        <input type="text" v-model="newTeam.team_member" placeholder="team_member" id="team_member">
      <div>
        팀 주제:
        <label for="theme"></label>
        <input type="text" v-model="newTeam.theme" placeholder="theme" id="theme">
      </div>
      <div>
        팀 공통 흥미:
        <label for="common_interest"></label>
        <input type="text" v-model="newTeam.common_interest" placeholder="common_interest" id="common_interest">
      </div>
      <div>
        팀 모집 인원:
        <label for="total_number"></label>
        <select v-model="total_number" aria-label="인원수를 선택하세요" class="form-select">
          <option value="0">모집 인원 선택(최대 6명)</option>
          <option value="5">5</option>
          <option value="6">6</option>
        </select>
      </div>
      <div>
        팀 카카오 오픈챗:
        <label for="kakao_chat"></label>
        <input type="text" v-model="newTeam.kakao_chat" placeholder="kakao_chat" id="kakao_chat">
      </div>
      <input type="submit">
    </form>

  </v-app>
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
        theme: this.team.theme,
        common_interest: this.team.common_interest,
        number: this.team.number,
        kakao_chat: this.team.kakao_chat,
        
      },

      total_number: this.team.total_number,

    }
  },

  computed: {
    ...mapGetters(['currentUser', 'allUsers',]),
  },


  methods: {
    ...mapActions(['updateTeam', 'fetchCurrentUser', 'fetchAllUsers']),
    onSubmit(){
      const payload = {
        id: this.team.id,
        leader: this.currentUser.id,
        total_number: this.total_number,
        common_interest: this.newTeam.common_interest,
        ...this.newTeam,
      }
      this.updateTeam(payload)
      alert("수정되었습니다.")
      },
    },

    

  created() {
    this.fetchCurrentUser()
  }
}
</script>

<style>

</style>