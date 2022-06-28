<template>
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <img src="@/assets/logo.png" alt="Avatar" style="width:300px;height:300px;">
    </div>
    <div class="flip-card-back">
      <div class="inner-content py-3 px-3 d-flex flex-column justify-content-evenly">
        <div class="each-content">
          닉네임: {{this.eachUser.nickname}} <a role="button" @click="followUser()"><i class="fa-solid fa-star"></i></a>
        </div>
        <div class="each-content">
          포지션: {{this.eachUser.position}}
        </div>
        <div class="each-content">
          전공여부: {{this.eachUser.major}}
        </div>
        <div class="each-content">
          성별: {{this.eachUser.sex}}
        </div>
        <div class="each-content">
          지역: {{this.eachUser.region}}
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name:'MemberList',
  props: {
    eachUser: {
      type:Object,
    },

  },
  computed: {
    ...mapGetters(['allUsers',])
  },
  methods: {
    ...mapActions(['fetchAllUsers', 'setBookmark',]),
    followUser() {
      this.setBookmark(this.eachUser.id)
    }
  },
  created() {
    this.fetchAllUsers()
  },
}
</script>

<style scoped>

.inner-content {
  height: 100%;
}

.each-content {
  border: 1px solid #f1f1f1;
  border-radius: 10px;
  background-color: white;
  margin: 1px;
  height: 40px;
  font-size: 18px;
  line-height: 40px;
}


.flip-card {
  background-color: transparent;
  width: 300px;
  height: 350px;
  /* border: 1px solid #f1f1f1; */
  perspective: 1000px;
  border-radius: 20px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  /* text-align: center; */
  transition: transform 0.8s;
  transform-style: preserve-3d;
  border-radius: 20px;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}

.flip-card-front {
  border-radius: 20px;
}

.flip-card-back {
  transform: rotateY(180deg);
  border-radius: 20px;
}
</style>