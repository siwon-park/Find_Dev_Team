<template>
  <div>
    <h1>팀 수정 페이지</h1>
    <TeamForm :team="team" action="update"></TeamForm>
  </div>
</template>

<script>
import TeamForm from '@/components/Teams/TeamForm.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'TeamEditView',
  components: { TeamForm },
  computed: {
    ...mapGetters(['team', ])
  },
  methods: {
    ...mapActions(['fetchTeam',])
  },
  created() {
    this.fetchTeam(this.$route.params.teamId)
  }

}
</script>

<style>

</style>