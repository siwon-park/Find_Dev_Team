<template>
  <div>
    <h1>팀 생성 페이지</h1>
    <TeamForm :team="team" action="create"></TeamForm>
  </div>
</template>

<script>
  import TeamForm from '@/components/TeamForm.vue'
  export default {
    name: 'TeamNewView',
    components: { TeamForm },
    data() {
      return {
        team: {
          pk: null,
          name:'',
          intro: '',
          leader: '',

        }
      }
    }

  }
</script>

<style>

</style>