<template>
  <div>
    <h1>팀 수정 페이지</h1>
    <TeamEditForm :team="team" action="update"></TeamEditForm>
  </div>
</template>

<script>
import TeamEditForm from '@/components/Teams/TeamEditForm.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'TeamEditView',
  components: { TeamEditForm },
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