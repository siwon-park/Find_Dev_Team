<template>
<!-- 전체 모달 화면-->
<div class="my-modal" @click="modalCloseOutside()">
  <!-- 보이는 화면 -->
  <div class="container modal-content">
    <div class="row">
      <div class="col d-flex justify-content-between">
        <div class="d-flex">
          <div class="circle" style="background-color: #c5af3d;">•</div>
          <div class="circle" style="background-color: #e3bfc8;">-</div>
          <div class="circle" style="background-color: #67769d;">+</div>
        </div>
        <div class="d-flex">
          <div class="rectangle mx-1" @click="modalCloseBtn()">X</div>
          <div class="arrow mx-1">◀</div>
        </div>
      </div>
    </div>
    <div class="row">
      <form @submit.prevent="signup(signup_credentials)">
        <div class="my-1">
          <span>유저이름: </span>
          <label for="username"></label>
          <input v-model="signup_credentials.username" type="text" id="username" placeholder="username" required/>
        </div>
        <div class="my-1">
          <span>비밀번호: </span>
          <label for="password1"></label>
          <input v-model="signup_credentials.password1" type="password" id="password1" placeholder="password1" required />
        </div>
        <div class="my-1">
          <span>비밀번호 확인: </span>
          <label for="password2"></label>
          <input v-model="signup_credentials.password2" type="password" id="password2" placeholder="password2" required />
        </div>
        <div class="my-1">
          <span>닉네임: </span>
          <label for="nickname"></label>
          <input v-model="signup_credentials.nickname" type="text" id="nickname" placeholder="nickname" required />
        </div>
        <div class="my-1">
          <span>지역: </span>
          <label for="region"></label>
          <input v-model="signup_credentials.region" type="text" id="region" placeholder="region" required />
        </div>
        <div class="my-1">
          <span>성별: </span>
          <label for="sex"></label>
          <input v-model="signup_credentials.sex" type="text" id="sex" placeholder="sex" required />
        </div>
        <div class="my-1">
          <span>포지션: </span>
          <label for="position"></label>
          <input v-model="signup_credentials.position" type="text" id="position" placeholder="position" required />
        </div>
        <div class="my-1">
          <span>전공: </span>
          <label for="major"></label>
          <input v-model="signup_credentials.major" type="text" id="major" placeholder="major" required />
        </div>
        <div class="my-1">
          <span>반: </span>
          <label for="group"></label>
          <input v-model="signup_credentials.group" type="text" id="group" placeholder="group" required />
        </div>
        <div class="my-3">
          <button class="btn">제출</button>
        </div>
      </form>
    </div>
  </div>
</div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'SignUpModal',
  props: {
    modalToggle: Boolean,
  },
  data() {
    return {
      signup_credentials: {
        username: '',
        password1: '',
        password2: '',
        sex: '',
        region: '',
        position: '',
        major: '',
        group: '', // 지역 반
        nickname: '',
      },

    }
  },
  methods: {
    ...mapActions(['signup',]),
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
    }
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

  .my-modal {
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    /* background-color: #474e5d;
    opacity: 0.4; */
    background-color: rgba(0, 0, 0, 0.6); /* 부모에게만 투명을 지정함 */
    padding-top: 50px;
  }

  #username, #password1, #password2, #nickname, #region, #sex, #position, #major, #group {
    background-color: white;
    border-radius: 5px;
    border: 1px solid black;
  }

  span {
    font: bold 20px sans-serif;
  }

  .btn {
    background-color: #DFFF80;
    border: 1px solid black;
    box-shadow: 3px 3px;
    transition: transform 200ms, box-shadow 200ms;
  }

  .btn:active {
    transform: translateY(4px) translateX(4px);
  }

  .col {
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

  .rectangle{
      height: 20px;
      width: 20px;
      background-color: #e33c3c;
      color: white;
      text-align: center;
      font-weight: bolder;
      border: 2px solid black;
      font-size: 15px;
      line-height: 15px;
      box-shadow: black 2px 2px 0px;
      transition: transform 100ms, box-shadow 100ms;
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
      color: white;
      text-align: center;
      font-weight: bolder;
      border: 2px solid black;
      font-size: 15px;
      line-height: 15px;
      box-shadow: black 2px 2px 0px;
      transition: transform 100ms, box-shadow 100ms;
    }

    .arrow:active{
      transform: translateY(2px) translateX(2px);
      box-shadow: black 0px 0px 0px;
    }

</style>