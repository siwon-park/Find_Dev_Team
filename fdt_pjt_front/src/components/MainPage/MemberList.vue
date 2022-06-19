<template>
  <div>
    {{this.eachUser}}
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name:'MemberList',
  props: {
    eachUser: {
      type:Object,
    }
  },
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