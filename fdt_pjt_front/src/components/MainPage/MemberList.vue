<template>
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <div class="box">
        <img src="@/assets/member.png" alt="Avatar" style="width:300px;height:300px;">
        <div class="text">{{ this.eachUser.nickname }}({{ this.eachUser.position }})</div>
      </div>
    </div>

    <div class="flip-card-back">
      <div class="inner-content py-3 px-3 d-flex flex-column justify-content-evenly">
        <div class="each-content">
          닉네임: {{this.eachUser.nickname}} <a role="button" @click="followUser()"><i class="fa-solid fa-star" v-bind:class="{ bookmark: isBookmarked }"></i></a>
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
        <div class="each-content">
          <a :href="this.eachUser.kakao_chat"> 카카오 오픈챗</a>
        </div>
        <div class="each-content">
          깃허브 : {{this.eachUser.github_url}}
        </div>
        <div class="each-content">
          소개 : {{this.eachUser.intro}}
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
    ...mapGetters(['allUsers', 'bookmarkings']),
    isBookmarked() {
      const bookmarkedUser = this.bookmarkings.bookmarking
      if (bookmarkedUser) {
        for (const userId of bookmarkedUser) {
          if (userId === this.eachUser.id) {
            return true
          }
        }
      }
      return false
    }
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

.box {
   position: relative;
}

.text {
   position: absolute;
   top: 50px;
   left: 100px;
   width: 100%;
   font-weight: bolder;
}

.inner-content {
  height: 100%;
  background-color: #fce2d1;
  width: 300px;
  height: 300px;
  border-radius: 20px;
  font-weight: bolder;
  text-align: center;
  box-shadow: inset -2px -2px 6px 0 rgba(255, 255, 255, 0.2),
    inset 2px 2px 6px 0 rgba(97, 97, 97, 0.8);
  
}

.each-content {
  font-size: 16px;
}

i {
    text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;  
}

.bookmark {
  color: yellow;
}

.flip-card {
  background-color: transparent;
  width: 300px;
  height: 350px;
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