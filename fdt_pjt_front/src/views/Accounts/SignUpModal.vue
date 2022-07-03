<template>
<!-- 전체 모달 화면-->
<div class="my-modal" @click="modalCloseOutside()">
  <!-- 보이는 화면 -->
  <div class="container modal-content">
    <div class="row">
      <div class="col d-flex justify-content-between" style="height:40px;">
        <div class="d-flex align-items-center">
          <div class="circle" style="background-color: #c5af3d;">•</div>
          <div class="circle" style="background-color: #e3bfc8;">-</div>
          <div class="circle" style="background-color: #67769d;">+</div>
        </div>
        <div class="d-flex align-items-center">
          <div class="rectangle mx-1" @click="modalCloseBtn()">X</div>
          <div class="arrow mx-1" @click="modalCloseBtn()">◀</div>
        </div>
      </div>
    </div>
    <div class="row">
      <form @submit.prevent="signup(signup_credentials)">
        <table>
          <tbody>
            <tr>
              <td>
                <label for="username">유저 네임</label>
              </td>
              <td>
                <input v-model="signup_credentials.username" type="text" id="username" placeholder="username" required/>
              </td>
            </tr>
            <tr>
              <td>
                <label for="password1">비밀번호</label>
              </td>
              <td>
                <input v-model="signup_credentials.password1" type="password" id="password1" placeholder="password1" required />
              </td>
            </tr>
            <tr>
              <td>
                <label for="password2">비밀번호 확인</label>
              </td>
              <td>
                <input v-model="signup_credentials.password2" type="password" id="password2" placeholder="password2" required />
              </td>
            </tr>
            <tr>
              <td>
                <label for="nickname">닉네임:</label>
              </td>
              <td>
                <input v-model="signup_credentials.nickname" type="text" id="nickname" placeholder="nickname" required />
              </td>
            </tr>
            <tr>
              <td>
                <label for="region">지역</label>
              </td>
              <td>
                <select v-model="signup_credentials.region" class="form-select" style="width:200px">
                  <option value="서울">서울</option>
                  <option value="대전">대전</option>
                  <option value="광주">광주</option>
                  <option value="부울경">부울경</option>
                  <option value="구미">구미</option>
                </select>
              </td>
            </tr>
            <tr>
              <td>
                <label for="sex">성별:</label>
              </td>
              <td>
                <select v-model="signup_credentials.sex" class="form-select" style="width:200px">
                  <option value="남">남</option>
                  <option value="여">여</option>
                </select>
              </td>
            </tr>
            <tr>
              <td>
                <label for="position">포지션:</label>
              </td>
              <td>
                <select v-model="signup_credentials.position" class="form-select" style="width:200px">
                  <option value="백엔드">백엔드</option>
                  <option value="프론트엔드">프론트엔드</option>
                </select>
              </td>
            </tr>
            <tr>
              <td>
                <label for="major">전공</label>
              </td>
              <td>
                <select v-model="signup_credentials.major" class="form-select" style="width:200px">
                  <option value="전공">전공</option>
                  <option value="비전공">비전공</option>
                </select>
              </td>
            </tr>
            <tr>
              <td>
                <label for="group">반</label>
              </td>
              <td>
                <select v-model="signup_credentials.group" class="form-select" style="width:200px">
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
              </td>
            </tr>
          </tbody>
        </table>
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
      window.addEventListener('click', (event) => {
        if (event.target === modal) {
          modal.style.display = "none"
          this.$emit('modal-close-btn', false)
        }
      })
    }
  }
}
</script>

<style scoped>
  .container {
    background-color: #fcf3e1;
    /* border: 2px solid black; */
    border-radius: 20px;
    box-shadow: 10px 10px;
    margin-top: 100px; 
    width: 50%;
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
      font-size: 15px;
      line-height: 15px;
      box-shadow: black 2px 2px 0px;
      transition: transform 100ms, box-shadow 100ms;
      cursor: pointer;
    }

    .arrow:active{
      transform: translateY(2px) translateX(2px);
      box-shadow: black 0px 0px 0px;
    }

  td {
    padding: 5px;
  }
</style>