<template>
<div class="my-modal" @click="modalCloseOutside()">
  <div class="container modal-content">
    <div class="d-flex" style="justify-content: right;">
      <div class="rectangle mx-1" @click="modalCloseBtn()">↩</div>
    </div>
    <div class="row">
      <table>
        <tbody>
          <tr>
            <td>
              <label for="name">팀 명</label>
            </td>
            <td>
              {{ this.eachTeamData.name }}
            </td>
          </tr>
          <tr>
            <td>
              <label for="intro">팀 소개</label>
            </td>
            <td>
              {{ this.eachTeamData.intro }}
            </td>
          </tr>
          <tr>
            <td>
              <label for="theme">팀 주제</label>
            </td>
            <td>
              {{ this.eachTeamData.theme }}
            </td>
          </tr>
          <tr>
            <td>
              <label for="common_interest">팀 공통흥미</label>
            </td>
            <td>
              {{ this.eachTeamData.common_interest }}
            </td>
          </tr>
          <tr>
            <td>
              <label for="total_number">현재 인원/모집 인원</label>
            </td>
            <td>
              {{ this.eachTeamData.number }}/{{ this.eachTeamData.total_number }}
            </td>
          </tr>
          <tr>
            <td>
              <label for="kakao_chat">팀 오픈챗</label>
            </td>
            <td>
              {{ this.eachTeamData.kakao_chat }}
            </td>
          </tr>
          <tr>
            <td>
              <label for="member">팀 멤버</label>
            </td>
            <td id="member">
              {{ this.eachTeamData.team_member }}
            </td>
          </tr>
          <tr>
            <td>
              <label for="leader">리더</label>
            </td>
            <td id="member">
              {{ this.eachTeamData.leader }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name:'TeamModal',
  props: {
    eachTeamData: {
      type: Object
    }
  },
  methods: {
    modalCloseBtn() {
      this.$emit('modal-close-btn', false)
    },
    modalCloseOutside() {
      const modal = document.querySelector('.my-modal')
      window.onclick = function (event) {
        if (event.target === modal) {
          modal.style.display = "none";
        }
      }
      this.$emit('modal-close', false)
    }
  },
}
</script>

<style scoped>
  .container {
    background-color: #e1f6fc;
    width: 40%;
    border: 10px solid #120c65
  }

  .my-modal {
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    overflow: auto;
    padding-top: 30px;
  }

  span {
    font: bold 20px sans-serif;
  }

  .col {
      background-color: #88d4f8;
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
    margin-top: 5px;
    margin-bottom: 5px;
    height: 25px;
    width: 25px;
    background-color: #4d3ce3;
    color: white;
    text-align: center;
    font-weight: bolder;
    font-size: 20px;
    line-height: 15px;
    box-shadow: black 2px 2px 0px;
    transition: transform 100ms, box-shadow 100ms;
    cursor: pointer;
    }

  .rectangle:active{
    transform: translateY(2px) translateX(2px);
    box-shadow: black 0px 0px 0px;
  }


  table{
    text-align: center;
    font-size: 20px;
  }


</style>