<template>
  <div class="my-modal" @click="modalCloseOutside()">
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
        <form @submit.prevent="updateRequest()">
          <div class="my-1">
            <label for="nickname">Nickname:</label>
            <input v-model="currentUser.nickname" type="text" id="nickname" required />
          </div>
          <div class="my-1">
            <label for="region">Region:</label>
            <input v-model="currentUser.region" type="text" id="region" required />
          </div>
          <div class="my-1">
            <label for="sex">Sex:</label>
            <input v-model="currentUser.sex" type="text" id="sex" required />
          </div>
          <div class="my-1">
            <label for="position">Position:</label>
            <input v-model="currentUser.position" type="text" id="position" required />
          </div>
          <div class="my-1">
            <label for="major">major:</label>
            <input v-model="currentUser.major" type="text" id="major" required />
          </div>
          <div class="my-1">
            <label for="group">group:</label>
            <input v-model="currentUser.group" type="text" id="group" required />
          </div>
          <div class="my-1">
            <label for="img">img:</label>
            <input v-model="currentUser.img" type="text" id="img" required />
          </div>
          <div class="my-1">
            <label for="intro">intro:</label>
            <input v-model="currentUser.intro" type="text" id="intro" required />
          </div>
          <div class="my-1">
            <label for="kakao_chat">kakao_chat:</label>
            <input v-model="currentUser.kakao_chat" type="text" id="kakao_chat" required />
          </div>
          <div class="my-1">
            <label for="github_url">github_url:</label>
            <input v-model="currentUser.github_url" type="text" id="github_url" required />
          </div>
          <div class="my-1">
            <label for="portfolio_url">portfolio_url:</label>
            <input v-model="currentUser.portfolio_url" type="text" id="portfolio_url" required />
          </div>
          <div class="my-1">
            <label for="strength">strength:</label>
            <input v-model="currentUser.strength" type="text" id="strength" required />
          </div>
          <!-- <div class="my-1">
            <label for="my_team">my_team:</label>
            <input v-model="currentUser" type="text" id="my_team" required />
          </div> -->
          <div class="my-3">
            <button class="btn">프로필 수정</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MyPageEdit',
  props: {
    modalToggle: Boolean,
  },
  data() {
    return {

    }
  },
  computed: {
    ...mapGetters(['currentUser','team',])
  },
  methods: {
    ...mapActions(['fetchCurrentUser', 'updateProfile', 'fetchTeam',]),
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
    updateRequest() {
      console.log(this.team, this.currentUser.my_team)
      const userData = {
          my_team: this.team,
          ...this.currentUser
        }
        // console.log(this.currentUser.my_team)
        this.updateProfile(userData)
    },
  },
  created() {
    this.fetchCurrentUser()
  },

  mounted(){
    this.fetchTeam(this.currentUser.my_team.id)
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

  #nickname, #region, #sex, #position, #major, #group, #img, #intro, #kakao_chat, #github_url, #portfolio_url, #strength {
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
    background-color: #DFFF80;
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