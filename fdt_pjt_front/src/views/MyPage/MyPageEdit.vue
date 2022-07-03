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
        <form @submit.prevent="updateRequest()">
          <table>
            <tbody>
              <tr>
                <td>
                  <label for="nickname">닉네임:</label>
                </td>
                <td>
                  <input v-model="currentUser.nickname" type="text" id="nickname" required />
                </td>
              </tr>
              <tr>
                <td>
                  <label for="region">지역:</label>
                </td>
                <td>
                  <select v-model="currentUser.region" class="form-select" style="width:164px">
                    <option value="서울">서울</option>
                    <option value="대전">대전</option>
                    <option value="광주">광주</option>
                    <option value="부울경">부울경</option>
                    <option value="구미">구미</option>
                  </select>
                  <!-- <input v-model="currentUser.region" type="text" id="region" required /> -->
                </td>
              </tr>
              <tr>
                <td>
                  <label for="sex">성별:</label>
                </td>
                <td>
                  <select v-model="currentUser.sex" class="form-select" style="width:164px">
                    <option value="남">남</option>
                    <option value="여">여</option>
                  </select>
                  <!-- <input v-model="currentUser.sex" type="text" id="sex" required /> -->
                </td>
              </tr>
              <tr>
                <td>
                  <label for="position">포지션:</label>
                </td>
                <td>
                  <select v-model="currentUser.position" class="form-select" style="width:164px">
                    <option value="백엔드">백엔드</option>
                    <option value="프론트엔드">프론트엔드</option>
                  </select>
                  <!-- <input v-model="currentUser.position" type="text" id="position" required /> -->
                </td>
              </tr>
              <tr>
                <td>
                  <label for="major">전공 여부:</label>
                </td>
                <td>
                  <select v-model="currentUser.major" class="form-select" style="width:164px">
                    <option value="전공">전공</option>
                    <option value="비전공">비전공</option>
                  </select>
                  <!-- <input v-model="currentUser.major" type="text" id="major" required /> -->
                </td>
              </tr>
              <tr>
                <td>
                  <label for="group">반: </label>
                </td>
                <td>
                  <select v-model="currentUser.group" class="form-select" style="width:164px">
                    <option value="1">1반</option>
                    <option value="2">2반</option>
                    <option value="3">3반</option>
                    <option value="4">4반</option>
                    <option value="5">5반</option>
                    <option value="6">6반</option>
                    <option value="7">7반</option>
                    <option value="8">8반</option>
                    <option value="9">9반</option>
                    <option value="10">10반</option>
                    <option value="11">11반</option>
                    <option value="12">12반</option>
                    <option value="13">13반</option>
                    <option value="14">14반</option>
                    <option value="15">15반</option>
                    <option value="16">16반</option>
                    <option value="17">17반</option>
                    <option value="18">18반</option>
                    <option value="19">19반</option>
                    <option value="20">20반</option>
                    <option value="21">21반</option>
                  </select>
                  <!-- <input v-model="currentUser.group" type="text" id="group" required /> -->
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
                  <label for="intro">소개:</label>
                </td>
                <td>
                  <input v-model="currentUser.intro" type="text" id="intro" required />
                </td>
              </tr>
              <tr>
                <td>
                  <label for="kakao_chat">카카오 오픈챗:</label>
                </td>
                <td>
                  <input v-model="currentUser.kakao_chat" type="text" id="kakao_chat" required />
                </td>
              </tr>
              <tr>
                <td>
                  <label for="github_url">github_url:</label>
                </td>
                <td>
                  <input v-model="currentUser.github_url" type="text" id="github_url" required />
                </td>
              </tr>
              <!-- <tr>
                <td>
                  <label for="portfolio_url">portfolio_url:</label>
                </td>
                <td>
                  <input v-model="currentUser.portfolio_url" type="text" id="portfolio_url" required />
                </td>
              </tr> -->
              <!-- <tr>
                <td>
                  <label for="strength">약점:</label>
                </td>
                <td>
                  <input v-model="currentUser.strength" type="text" id="strength" required />
                </td>
              </tr> -->
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
      window.addEventListener('click', (event) => {
        if (event.target === modal) {
          modal.style.display = "none"
          this.$emit('modal-close-btn', false)
        }
      })
      // window.onclick = function (event) {
      //   if (event.target === modal) {
      //     modal.style.display = "none";
      //     this.$emit('modal-close-btn', false)
      //   }
      // }
    },
    updateRequest() {
      console.log(this.team, this.currentUser.my_team)
      const userData = {
          my_team: this.team,
          ...this.currentUser
        }
        // console.log(this.currentUser.my_team)
        this.updateProfile(userData)
        this.$emit('modal-close-btn', false)
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
  .my-modal {
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.6); /* 부모에게만 투명을 지정함 */
    padding-top: 100px;
  }

  .container {
    background-color: #fcf3e1;
    /* border: 2px solid black; */
    border-radius: 20px;
    box-shadow: 10px 10px; 
    width: 40%;
  }

  #nickname, #region, #sex, #position, #major, #group, #img, #intro, #kakao_chat, #github_url, #portfolio_url, #strength {
    background-color: white;
    border-radius: 5px;
    /* border: 1px solid black; */
  }

  span {
    font: bold 20px sans-serif;
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