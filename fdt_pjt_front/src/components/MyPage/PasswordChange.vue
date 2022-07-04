<template>
  <div class="my-modal2" @click="modalCloseOutside()">
    <div class="container modal-content">
      <div class="row">
        <div class="col d-flex">
          <div class="d-flex" >
            <div class="circle" style="background-color: #c5af3d;">•</div>
            <div class="circle" style="background-color: #e3bfc8;">-</div>
            <div class="circle" style="background-color: #67769d;">+</div>
          </div>
          <div class="d-flex">
            <div class="rectangle" @click="modalCloseBtn()">X</div>
            <div class="arrow" @click="modalCloseBtn()">◀</div>
          </div>
        </div>
        <div class="row">
          <form @submit.prevent="changeSubmit(passwordData.password1, passwordData.password2)" action="POST">
            <table>
              <tbody>
                <tr>
                  <td>
                    <label for="password1">새 비밀번호</label>
                  </td>
                  <td>
                    <input type="password" v-model="passwordData.password1" placeholder="새 비밀번호" id="password1">
                  </td>
                </tr>
                <tr>
                  <td>
                    <label for="password2">비밀번호 확인</label>
                  </td>
                  <td>
                    <input type="password" v-model="passwordData.password2" placeholder="비밀번호 확인" id="password2">
                  </td>
                </tr>
              </tbody>
            </table>
            <div class="my-3">
              <button class="btn">비밀번호 변경하기</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'PasswordChange',
  data() {
    return {
      passwordData: {
        password1: '',
        password2: '',
      }
    }
  },
  methods: {
    ...mapActions(['changePassword',]),
    changeSubmit(p1, p2) {
      this.changePassword({password1: p1, password2: p2})
      this.$emit('modal-close-btn2', false)
    },
    modalCloseBtn() {
      this.$emit('modal-close-btn2', false)
    },
    modalCloseOutside() {
      const modal = document.querySelector('.my-modal2') // my-modal에 대한 부분만 선택 됨
      window.addEventListener('click', (event) => {
        if (event.target === modal) {
          modal.style.display = 'none'
          this.$emit('modal-close-btn2', false)
        }
      })
    },
  }
}
</script>

<style scoped>
  .my-modal2 {
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
    border-radius: 20px;
    box-shadow: 10px 10px; 
    width: 40%;
    margin-top: 100px; 
  }

  #password1, #password2 {
    background-color: white;
    border-radius: 5px;
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