<template>
  <div>
    <div class="card" style="width: 18rem;">
      <img src="" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">팀 이름: {{ this.eachTeam.name }}</h5>
        <p class="card-text">팀 소개: {{ this.eachTeam.intro }}</p>
        <!-- <div class="card-text">
          <div>팀 소개: {{ this.eachTeam.intro }}</div>
          <p v-for="member in eachTeam.team_member" :key="member.id">
            팀원: {{ member.username }}
          </p>
          <div>팀 주제: {{ eachTeam.theme }}</div>
          <div>팀 관심사: {{ eachTeam.theme }}</div>
          
        </div> -->
        <!-- <p class="card-text">팀 소개: {{ this.eachTeam }}</p> -->
        <a type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">자세히 보기</a>
        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <!-- <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel"></h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
              </div>
            </div> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import TeamModal from '@/components/MainPage/TeamModal'

export default {
  name: 'TeamList',
  components: {
    // TeamModal
  },
  props: {
    eachTeam: {
      type: Object,
    } 
  },
  
}
</script>

<style>

</style>