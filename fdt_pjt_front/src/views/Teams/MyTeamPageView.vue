<template>
  <div>
    <div class="title">팀 {{ team.name }} 페이지</div>
    <div class="container">
      <div class="row">
        <div class="col d-flex">
          <div class="d-flex" >
            <div class="circle" style="background-color: #c5af3d;">•</div>
            <div class="circle" style="background-color: #e3bfc8;">-</div>
            <div class="circle" style="background-color: #67769d;">+</div>
          </div>
          <div class="d-flex">
            <div class="rectangle" @click="goBack">X</div>
            <div class="arrow" @click="goBack">◀</div>
          </div>
        </div>
        <div class="first">
          <div>
            팀 명 : {{ team.name }}<br>
            팀 소개 : {{ team.intro }}<br>
            팀 소개 : {{ team.intro }}<br>
            주제 : {{ team.theme }}<br>
            흥미 : {{ team.common_interest }}<br>
            현재 인원 수 : {{ team.team_member.length }}<br>
            모집 인원 : {{ team.total_number }}<br>
            <a :href="team.kakao_chat"> 카카오 오픈챗</a>
            팀 멤버 :
            <span>
              <span v-for="name in teamMemberName" :key="name">
                <span class="mx-1">{{name}}</span>
              </span>
            </span>
          </div>
        </div>
        <button>
          <div @click="openModal()" class="update">팀 정보 수정</div>
        </button>
        

        <!-- <div>
          <router-link :to="{ name: 'teamEdit', params: { teamId } }">
            <button>팀 수정 버튼</button>
          </router-link>
        </div> -->
        
      </div>
      <TeamEditForm v-if="modalToggle" :team="team" :modalToggle="modalToggle" @modal-close-btn="closeModal()"></TeamEditForm>
    </div>
    <!-- modal -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import TeamEditForm from '@/components/Teams/TeamEditForm.vue'
import router from '@/router'

export default {
  name: 'MyTeamPageView',
  components: {
    TeamEditForm,
  },
  data() {
    return{
      modalToggle: false,
      teamId: this.$route.params.teamId,
    }
  },
  computed:{
    ...mapGetters(['team']),
    teamMemberName() {
      const nameList = []
      for (const user of this.team.team_member) {
        nameList.push(user.username)
      }
      return nameList
    }
  },
  methods:{
    ...mapActions([
      'fetchTeam',
    ]),
    openModal(){
      this.modalToggle = !this.modalToggle
    },
    closeModal() {
      this.modalToggle = false
    },
    goBack() {
        router.push({ name: 'main' })
      }
  },
  created(){
    this.fetchTeam(this.teamId)
  },
}
</script>

<style scoped>
  
  .container {
    background-color: #fcf3e1;
    /* border: 2px solid black; */
    border-radius: 20px;
    box-shadow: 10px 10px;
    width: 700px;
  }

  .title{
    font-family: 'Gowun Dodum', sans-serif;
    font-weight: bolder;
    font-size: 60px;
    text-align: center;
    padding-bottom: 35px;
    color: #FDFDFD;
    text-shadow: #E3B8D3 1px 1px,#E3B8D3 0px 0px,#E3B8D3 1px 1px,#E3B8D3 2px 2px,#E3B8D3 3px 3px,#E3B8D3 4px 4px,#E3B8D3 5px 5px,#E3B8D3 6px 6px,#E3B8D3 7px 7px,#E3B8D3 8px 8px,#E3B8D3 9px 9px,#E3B8D3 10px 10px,#E3B8D3 11px 11px,#E3B8D3 12px 12px,#E3B8D3 13px 13px,#E3B8D3 14px 14px,#E3B8D3 15px 15px,#E3B8D3 16px 16px,#E3B8D3 17px 17px,#E3B8D3 18px 18px,#E3B8D3 19px 19px,#E3B8D3 20px 20px;

  }

  .row{
    padding-bottom: 20px;
  }

  .col{
    background-color: #f7d1ff;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    justify-content: space-between;
    height: 45px;
  }

  .first{
    justify-content: space-between;
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
    transition: transform 100ms, box-shadow 100ms;
    color: white;
    text-align: center;
    font-weight: bolder;
    /* border: 2px solid black; */
    font-size: 15px;
    line-height: 15px;
    box-shadow: black 2px 2px 0px;
    margin-right: 10px;
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
    transition: transform 100ms, box-shadow 100ms;
    color: white;
    text-align: center;
    font-weight: bolder;
    /* border: 2px solid black; */
    font-size: 15px;
    line-height: 15px;
    box-shadow: black 2px 2px 0px;
    cursor: pointer;
    margin-top: 10px;
    
  }

  .arrow:active{
    transform: translateY(2px) translateX(2px);
    box-shadow: black 0px 0px 0px;
  }

  button{
    background-color: #DFFF80;
    box-shadow: black 4px 4px 0px;
    /* border: 2px solid black; */
    border-radius: 8px;
    transition: transform 200ms, box-shadow 200ms;
    width : 120px;
    height: 35px;
    margin: auto;
    
  }

  button:active{
    transform: translateY(4px) translateX(4px);
    box-shadow: black 0px 0px 0px;
  }

  .update{
    text-decoration: none;
    color:black;
  }

  @media(max-width:768px){
    .container{
      width: 50%;
      display: grid;
    }
    .first{
      flex-direction: column;
    }


  }
</style>