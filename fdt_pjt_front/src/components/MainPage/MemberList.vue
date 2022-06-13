<template>
  <div>
    {{ allUsers }}
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name:'MemberList',

  computed: {
    ...mapGetters(['allUsers',])
  },
  methods: {
    ...mapActions(['fetchAllUsers',])
  },
  created() {
    this.fetchAllUsers()
  }
}
</script>

<style>

</style>