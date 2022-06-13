<template>
  <div>
    {{ teams }}
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'TeamList',
  methods: {
    ...mapActions(['fetchTeams',])
  },
  computed: {
    ...mapGetters(['teams',])
  },
  created() {
    this.fetchTeams()
  }

}
</script>

<style>

</style>