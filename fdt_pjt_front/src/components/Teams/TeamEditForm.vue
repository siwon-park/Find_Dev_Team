<template>
  <div class="my-modal" @click="modalCloseOutside()">
    <div class="container modal-content">
      <div class="row">
        <div class="col d-flex">
          <div class="d-flex">
            <div class="circle" style="background-color: #c5af3d;">•</div>
            <div class="circle" style="background-color: #e3bfc8;">-</div>
            <div class="circle" style="background-color: #67769d;">+</div>
          </div>
          <div class="d-flex">
            <div class="rectangle mx-1" @click="modalCloseBtn()">X</div>
            <div class="arrow mx-1" @click="modalCloseBtn()">◀</div>
          </div>
        </div>
      </div>
      <div class="row">
        <form @submit.prevent="onSubmit()">
          <table>
            <tbody>
              <tr>
                <td>
                  <label for="name">팀 명:</label>
                </td>
                <td>
                  <input v-model="newTeam.name" type="text" id="name" placeholder="name" >
                </td>
              </tr>
              <tr>
                <td>
                  <label for="intro">팀 소개</label>
                </td>
                <td>
                  <input type="text" v-model="newTeam.intro" placeholder="intro" id="intro">
                </td>
              </tr>
              <tr>
                <td>
                  <label for="theme">팀 주제</label>
                </td>
                <td>
                  <input type="text" v-model="newTeam.theme" placeholder="theme" id="theme">
                </td>
              </tr>
              <tr>
                <td>
                  <label for="common_interest">팀 공통흥미</label>
                </td>
                <td>
                  <input type="text" v-model="newTeam.common_interest" placeholder="common_interest" id="common_interest">
                </td>
              </tr>
              <tr>
                <td>
                  <label for="total_number">팀 모집 인원</label>
                </td>
                <td>
                  <select v-model="total_number" aria-label="인원수를 선택하세요" class="form-select">
                    <option value="0">모집 인원 선택(최대 6명)</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td>
                  <label for="kakao_chat">팀 오픈챗</label>
                </td>
                <td>
                  <input type="text" v-model="newTeam.kakao_chat" placeholder="kakao_chat" id="kakao_chat">
                </td>
              </tr>
              <tr>
                <td>
                  <label for="img">프로필 이미지: </label>
                </td>
                <td>
                  <input v-model="currentUser.img" type="text" id="img" required />
                </td>
              </tr>
              <tr>
                <td>
                  <label for="member">팀 멤버</label>
                </td>
                <td id="member">
                  <span v-for="teamMemberName in currentTeamMember" :key="teamMemberName">
                    <span class="mx-1">{{teamMemberName}}</span>
                  </span>
                  <span v-for="tempTeamMemberName in this.tempTeamMembersForRender" :key="tempTeamMemberName">
                    <span class="mx-1">{{tempTeamMemberName}}</span>
                  </span>
                </td>
              </tr>
              <tr>
                <td>
                  <label>팀 멤버 검색</label>
                </td>
                <td>
                  <section id="searchbar-section">        
                    <input
                      type="text" 
                      @input="inputChange"
                      v-model="keyInput"
                      id="member"
                    >
                    <button style="margin-left:10px;">검색</button>
                  </section>
                  <div v-if="keyInput !== ''">
                    <ul v-for="(ret, index) in keyword" :key="index">
                      <li @click="addTeamMember(ret)">{{ ret.username }}</li>
                    </ul>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="my-3">
            <button class="btn">수정하기</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'TeamForm',
  props:{
    modalToggle: Boolean,
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
      keyInput: '',
      tempTeamMembers: [], // 데이터 저장용
      tempTeamMembersForRender: [], // 렌더링용
    }
  },

  computed: {
    ...mapGetters(['currentUser', 'allUsers', 'keyword']),
    currentTeamMember() {
      const curTM = []
      for (const member of this.team.team_member) {
        curTM.push(member.username)
      }
      return curTM
    }
  },

  methods: {
    ...mapActions(['updateTeam', 'fetchCurrentUser', 'fetchAllUsers', 'searchMember']),
    modalCloseBtn() {
      this.$emit('modal-close-btn', false)
    },
    modalCloseOutside() {
      const modal = document.querySelector('.my-modal') // my-modal에 대한 부분만 선택 됨
      window.onclick = function (event) {
        if (event.target === modal) {
          modal.style.display = "none";
        }
      }
    },
    onSubmit(){
      this.newTeam.team_member.push(...this.tempTeamMembers)
      const payload = {
        id: this.team.id,
        leader: this.currentUser.id,
        total_number: this.total_number,
        team_member: this.newTeam.team_member,
        common_interest: this.newTeam.common_interest,
        ...this.newTeam,
      }
      this.updateTeam(payload)
      this.$emit('modal-close-btn', false)
      alert("수정되었습니다.")
    },

    inputChange(event) {
      this.searchMember(event.target.value)
    },

    // 유저를 추가 및 삭제
    addTeamMember(member) {
      let flag = false
      let idx = 0
      for (const addUser of this.tempTeamMembers) {
        if (addUser === member) {
          flag = true
          idx = this.tempTeamMembers.indexOf(addUser)
          break
        }
      }
      if (!flag) {
        this.tempTeamMembers.push(member)
        this.tempTeamMembersForRender.push(member.username)
      } else {
        this.tempTeamMembers.splice(idx, 1)
        this.tempTeamMembersForRender.splice(idx, 1)
      }
    }
  },

    

  created() {
    this.fetchCurrentUser()
  }
}
</script>

<style scoped>
  .my-modal {
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.6); /* 부모에게만 투명을 지정함 */
    padding-top: 50px;
  }

  .container {
    background-color: #fcf3e1;
    /* border: 2px solid black; */
    border-radius: 20px;
    box-shadow: 10px 10px; 
    width: 40%;
  }

  #name, #intro, #theme, #member, #common_interest, #total_number, #img, #intro, #kakao_chat, #github_url, #portfolio_url, #strength {
    background-color: white;
    border-radius: 5px;
    /* border: 1px solid black; */
  }

  .btn {
    background-color: #DFFF80;
    /* border: 1px solid black; */
    box-shadow: 3px 3px;
    transition: transform 200ms, box-shadow 200ms;
  }

  .btn:active {
    transform: translateY(4px) translateX(4px);
    background-color: #DFFF80;
  }

  .col {
      background-color: #f7d1ff;
      border-top-left-radius: 20px;
      border-top-right-radius: 20px;
      justify-content: space-between;
      height: 45px;
  }

  .circle{
      border-radius: 50%;
      height: 20px;
      width: 20px;
      color: black;
      text-align: center;
      font-weight: bolder;
      /* border: 2px solid black; */
      font-size: 14px;
      margin-right: 10px;
      line-height: 15px;
      margin-top: 10px;
    }

  .rectangle{
      height: 20px;
      width: 20px;
      background-color: #e33c3c;
      color: white;
      text-align: center;
      font-weight: bolder;
      /* border: 2px solid black; */
      font-size: 15px;
      line-height: 15px;
      box-shadow: black 2px 2px 0px;
      transition: transform 100ms, box-shadow 100ms;
      cursor: pointer;
      margin-top: 10px;
    }

  .rectangle:active{
    transform: translateY(2px) translateX(2px);
    box-shadow: black 0px 0px 0px;
  }

  .arrow{
      height: 20px;
      width: 20px;
      background-color: rgb(43, 154, 69);
      color: white;
      text-align: center;
      font-weight: bolder;
      /* border: 2px solid black; */
      font-size: 15px;
      line-height: 15px;
      box-shadow: black 2px 2px 0px;
      transition: transform 100ms, box-shadow 100ms;
      cursor: pointer;
      margin-top: 10px;
    }

  .arrow:active{
    transform: translateY(2px) translateX(2px);
    box-shadow: black 0px 0px 0px;
  }

  td {
    padding: 5px;
  }

</style>