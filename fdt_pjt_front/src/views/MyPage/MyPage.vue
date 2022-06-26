<template>
  <div>
    <div class="title">{{ this.currentUser.username }}님의 프로필 페이지</div>
    <div class="container">
      <!-- 사진 및 기본 정보  -->
      <div class="row">
        <div class="col d-flex">
          <div class="d-flex title">
            <!-- <div>나의 프로필</div> -->
            <div class="circle" style="background-color: #c5af3d;">•</div>
            <div class="circle" style="background-color: #e3bfc8;">-</div>
            <div class="circle" style="background-color: #67769d;">+</div>
          </div>
          <div class="d-flex">
            <div class="rectangle" @click="modalCloseBtn()">X</div>
            <div class="arrow">◀</div>
          </div>
        </div>
        <div class="first d-flex">
          <div>
            {{ this.currentUser.img }}
          </div>
          <div>
            이름 : {{ this.currentUser.username }}<br>
            성별 : {{ this.currentUser.sex }}<br>
            지역 : {{ this.currentUser.region }}<br>
            반 : {{ this.currentUser.group }}<br>
            포지션(B/F) : {{ this.currentUser.position }}<br>
            전공 : {{ this.currentUser.major }}
          </div>
        </div>
        <!-- 부가 정보 -->
        <div>
          소개 : {{ this.currentUser.intro }}<br>
          오픈 카카오 : {{ this.currentUser.kakao_chat }}<br>
          GitHub : {{ this.currentUser.github_url }}<br>
          포트폴리오 url : {{ this.currentUser.portfolio_url }}<br>
          약점 : {{ this.currentUser.strength }}<br>
          팀 : {{ this.currentUser.my_team.name }}
        </div>
        <button>
          <!-- <router-link class="update" to="/mypage/edit">프로필 수정</router-link> -->
          <div @click="openModal()" class="update">프로필 수정</div>
        </button>
      </div>
    </div>
    <MyPageEdit v-if="modalToggle" :modalToggle="modalToggle" @modal-close-btn="closeModal()"></MyPageEdit>
  </div>
    
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MyPageEdit from '@/views/MyPage/MyPageEdit.vue'

export default {
  name: 'MyPage',
  components: {
    MyPageEdit,
  },
  data() {
    return {
      modalToggle: false,
    }
  },
  computed: {
    ...mapGetters(['currentUser',])
  },
  methods: {
    ...mapActions(['fetchCurrentUser',]),
    openModal(){
      this.modalToggle = !this.modalToggle
    },
    closeModal(data) {
      this.modalToggle = data
    }
  },
  created() {
    this.fetchCurrentUser()
  }
}
</script>

<style scoped>
  .container {
    background-color: #fcf3e1;
    border: 2px solid black;
    border-radius: 20px;
    box-shadow: 5px 5px;
    width: 700px;
  }

  .title{
    font-weight: bolder;
    font-size: 40px;
    text-align: center;
    padding-bottom: 15px;
    color: white;
    /* -webkit-text-stroke: 1px #b437dd; */
    text-shadow: #b437dd 4px 4px 5px;

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
    border: 2px solid black;
    font-size: 14px;
    margin-right: 10px;
    line-height: 15px;
  }

  .rectangle{
    height: 20px;
    width: 20px;
    background-color: #e33c3c;
    transition: transform 100ms, box-shadow 100ms;
    color: white;
    text-align: center;
    font-weight: bolder;
    border: 2px solid black;
    font-size: 15px;
    line-height: 15px;
    box-shadow: black 2px 2px 0px;
    margin-right: 10px;
    cursor: pointer;
    
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
    border: 2px solid black;
    font-size: 15px;
    line-height: 15px;
    box-shadow: black 2px 2px 0px;
    cursor: pointer;
    
  }

  .arrow:active{
    transform: translateY(2px) translateX(2px);
    box-shadow: black 0px 0px 0px;
  }

  button{
    background-color: #DFFF80;
    box-shadow: black 4px 4px 0px;
    border: 2px solid black;
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