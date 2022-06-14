<template>
  <div>
    <h1>팀 생성 페이지</h1>
    <TeamCreateForm :team="team" action="create"></TeamCreateForm>
  </div>
</template>

<script>
  import TeamCreateForm from '@/components/Teams/TeamCreateForm.vue'
  export default {
    name: 'TeamNewView',
    components: { TeamCreateForm },
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