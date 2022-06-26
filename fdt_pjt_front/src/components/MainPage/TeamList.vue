<template>
<div>
  <div class="container">
    <div class="row">
      <div class="col d-flex align-items-center" style="height:40px;">
        <div class="circle" style="background-color: #c5af3d;">•</div>
        <div class="circle" style="background-color: #e3bfc8;">-</div>
        <div class="circle" style="background-color: #67769d;">+</div>
      </div>
    </div>
    <div class="row">
      <h5 class="card-title">팀 이름: {{ this.eachTeam.name }}</h5>
      <p class="card-text">팀 소개: {{ this.eachTeam.intro }}</p>
      <div class="d-flex justify-content-left">
          <button class="btn" @click="openModal()">자세히보기</button>
      </div>
    </div>
  </div>
  <TeamModal
  v-if="modalToggle"
  :modalToggle="modalToggle"
  :eachTeamData="this.eachTeam"
  @modal-close-btn="closeModal()"
  @modal-close="closeModal()"
  ></TeamModal>
</div>
</template>

<script>
import TeamModal from '@/components/MainPage/TeamModal'

export default {
  name: 'TeamList',
  components: {
    TeamModal
  },
  props: {
    eachTeam: {
      type: Object,
    } 
  },
  data() {
    return {
      modalToggle: false,
    }
  },
  methods: {
    openModal() {
      this.modalToggle = !this.modalToggle
      const body = document.querySelector('body')
      body.style.backgroundColor = "rgba(0, 0, 0, 0.6)"
    },
    closeModal(data) {
      this.modalToggle = data
      const body = document.querySelector('body')
      body.style.backgroundColor = "rgba(255, 255, 255)"
    },
  },
}
</script>

<style scoped>
.container {
  background-color: #fcf3e1;
  border: 2px solid black;
  border-radius: 20px;
  box-shadow: 5px 5px;
  width: 500px;
  height: 300px;
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

span {
  font: small-caps bold 20px sans-serif;
}

a {
  text-decoration: none;
  color: black;
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

</style>