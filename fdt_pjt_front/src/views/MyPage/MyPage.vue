<template>
  <div>
    <h1>나의 프로필 페이지</h1>
    <div class="container" style="width: 700px; height: 470px; margin:0 auto">
      <!-- 사진 및 기본 정보  -->
      <div class="row">
        <div class="col d-flex" style="height:40px;">
          <div class="circle" style="background-color: #c5af3d;">•</div>
          <div class="circle" style="background-color: #e3bfc8;">-</div>
          <div class="circle" style="background-color: #67769d;">+</div>
        </div>
        <div class="d-flex justify-content-between">
          <div style="width: 300px; height: 220px;">
            {{ this.currentUser.img }}
          </div>
          <div style="margin-right: 150px; margin-top:20px">
            이름 : {{ this.currentUser.username }}<br>
            성별 : {{ this.currentUser.sex }}<br>
            지역 : {{ this.currentUser.region }}<br>
            반 : {{ this.currentUser.group }}<br>
            포지션(B/F) : {{ this.currentUser.position }}<br>
            전공 : {{ this.currentUser.major }}
          </div>
        </div>
        <!-- 부가 정보 -->
        <div style="margin-left: 20px;">
          소개 : {{ this.currentUser.intro }}<br>
          오픈 카카오 : {{ this.currentUser.kakao_chat }}<br>
          GitHub : {{ this.currentUser.github_url }}<br>
          포트폴리오 url : {{ this.currentUser.portfolio_url }}<br>
          약점 : {{ this.currentUser.strength }}<br>
          팀 : {{ this.currentUser.my_team.name }}
        </div>
        <button>
          <router-link style="text-decoration: none; color:black;" to="/mypage/edit">프로필 수정</router-link>
        </button>
      </div>
    </div>
    
    
  </div>
    
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MyPage',
  computed: {
    ...mapGetters(['currentUser',])
  },
  methods: {
    ...mapActions(['fetchCurrentUser',])

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
  }

  .col{
    background-color: #f7d1ff;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
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

  button{
    background-color: #DFFF80;
    box-shadow: black 4px 4px 0px;
    border: 2px solid black;
    border-radius: 8px;
    transition: transform 200ms, box-shadow 200ms;
    color : black;
    width : 120px;
    height: 35px;
    margin: auto;
    
  }

  button:active{
    transform: translateY(4px) translateX(4px);
    box-shadow: black 0px 0px 0px;
  }
</style>