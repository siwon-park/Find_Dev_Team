<template>
<div>
  <div class="container" >
    <div class="row top">
      <div class="col d-flex align-items-center">{{ this.eachTeam.number }}/{{ this.eachTeam.total_number }}</div>
    </div>
    <div class="row new">
      <div class="content-title">{{ this.eachTeam.name }}</div>
      <div class="content-text">{{ this.eachTeam.intro }}</div>
      <div class="content-btn">
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
.new {
  background-color: #ffe08b;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
  border-bottom-left-radius: 20px;
  box-shadow: 10px 10px;
  width: 500px;
  height: 300px;
}

.col {
    background-color: #edca67;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    height: 40px;
}

.btn {
  background-color: #76b9ed;
  box-shadow: 3px 3px;
  transition: transform 200ms, box-shadow 200ms;
  height: 40px;
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

.top {
  width: 230px;
}

.content-title{
  font-size: 30px;
  text-align: center;
  margin-top: 10%;
}

.content-text{
  font-size: 25px;
  text-align: center;
  
}

.content-btn{
  text-align: center;
}

</style>