<template>
<div class="my-modal" @click="modalCloseOutside()">
  <div class="container modal-content">
    <div class="row">
      <div class="col d-flex justify-content-between align-items-center" style="height:40px;">
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
      <h5>팀 이름: {{ this.eachTeamData.name }}</h5>
      <p>팀 소개: {{ this.eachTeamData.intro }}</p>
      {{this.eachTeamData}}
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
    height: 100vh;
    overflow: auto;
    padding-top: 50px;
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